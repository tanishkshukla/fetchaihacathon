"""
CampusMitra AI - Multi-Agent LangGraph & Python Orchestrator
Coordinates TimetableAgent, NavigationAgent, FacultyAgent, MessCanteenAgent, and RAGAgent,
and packages responses with ASI:One Interactive Cards protocol.
"""
import json
import re
from typing import Dict, Any, Tuple

from .timetable_agent import TimetableAgent
from .navigation_agent import NavigationAgent
from .faculty_agent import FacultyAgent
from .mess_canteen_agent import MessCanteenAgent
from .rag_agent import RAGAgent
from ..cards.card_builder import (
    main_menu_carousel,
    timetables_year_carousel,
    timetable_schedule_detail,
    mess_days_carousel,
    mess_detail_card,
    canteen_carousel,
    canteen_category_detail_card,
    buildings_carousel,
    building_detail_card,
    faculty_carousel,
    faculty_detail_card,
    rag_result_card,
)


class CampusMitraOrchestrator:
    def __init__(self):
        self.timetable_agent = TimetableAgent()
        self.navigation_agent = NavigationAgent()
        self.faculty_agent = FacultyAgent()
        self.mess_canteen_agent = MessCanteenAgent()
        self.rag_agent = RAGAgent()

    def parse_input(self, raw_input: str) -> Tuple[str, Dict[str, Any]]:
        """Parses JSON action payload from ASI:One card clicks, or plain natural text."""
        raw_clean = raw_input.strip()
        if raw_clean.startswith("{") and raw_clean.endswith("}"):
            try:
                payload = json.loads(raw_clean)
                return "card_action", payload
            except Exception:
                pass
        return "text_query", {"query": raw_clean}

    def route_intent(self, text: str, context: Dict[str, Any]) -> str:
        """Classifies intent using semantic keywords and context."""
        lower = text.lower()

        # Check action payloads
        action = context.get("action", "")
        if action.startswith("menu_mess") or action.startswith("view_mess"):
            return "MESS"
        if action.startswith("menu_canteen") or action.startswith("view_canteen"):
            return "CANTEEN"
        if action.startswith("menu_timetables") or action.startswith("select_year") or action.startswith("view_timetable"):
            return "TIMETABLE"
        if action.startswith("menu_buildings") or action.startswith("view_building"):
            return "NAVIGATION"
        if action.startswith("menu_faculty") or action.startswith("view_faculty"):
            return "FACULTY"
        if action.startswith("menu_rag"):
            return "RAG"
        if action.startswith("main_menu") or lower in {"hi", "hello", "start", "menu", "help", "home"}:
            return "MAIN_MENU"

        # Check natural text keywords
        # 1. Mess & Food keywords
        if any(w in lower for w in ["mess", "hostel food", "breakfast", "lunch", "dinner", "kheer", "paratha", "chole bhature", "jalebi", "gulab jamun", "dahi", "bhaji"]):
            return "MESS"

        # 2. Canteen & Fast Food keywords
        if any(w in lower for w in ["canteen", "burger", "momo", "cold drink", "cold coffee", "coffee", "tea", "chai", "fries", "maggi", "sandwich", "coke", "thums up", "sprite", "frappe"]):
            return "CANTEEN"

        # 3. Faculty keywords
        if any(w in lower for w in ["faculty", "professor", "prof", "hod", "cabin", "teacher", "visiting hours", "office hours", "lokesh", "atma rai", "himanshu", "deepak arya", "dimpi", "ranjan", "bhanupriya", "vipin", "priti saini"]):
            return "FACULTY"

        # 4. Timetable keywords
        if any(w in lower for w in ["timetable", "schedule", "class today", "classes", "lecture", "period", "routine", "timing", "1st year", "2nd year", "3rd year", "4th year", "cse aiml", "gfg", "ibm"]):
            return "TIMETABLE"

        # 5. Navigation & Building keywords
        if any(w in lower for w in ["room", "block", "floor", "building", "hall", "lab", "b-001", "c-202", "c-212", "d-202", "locate", "where is", "map"]):
            return "NAVIGATION"

        # 6. Handbook & Policies
        if any(w in lower for w in ["attendance", "condonation", "detention", "marks", "exam", "rule", "policy", "handbook", "grading", "gpa", "cgpa", "fee", "wifi"]):
            return "RAG"

        return "MAIN_MENU"

    def process_request(self, user_msg: str, session: Dict[str, Any]) -> Dict[str, Any]:
        """
        Master multi-agent execution pipeline.
        """
        msg_type, payload = self.parse_input(user_msg)
        query_text = payload.get("query", user_msg) if msg_type == "text_query" else payload.get("action", "")
        
        active_context = {**session, **payload}
        intent = self.route_intent(query_text, active_context)

        # --------------------------------------------------------------------
        # ROUTE 1: HOSTEL MESS FOOD
        # --------------------------------------------------------------------
        if intent == "MESS":
            action = active_context.get("action", "")
            if action == "view_mess" or any(d in query_text.lower() for d in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]):
                res = self.mess_canteen_agent.handle(query_text, active_context)
                card = mess_detail_card(res["day"])
                return {
                    "text": res["text"],
                    "card_kind": "detail",
                    "card_payload": card,
                    "agent_used": "MessCanteenAgent",
                    "session_updates": {"mess_day": res["day"], "last_intent": "MESS"}
                }

            card = mess_days_carousel()
            return {
                "text": "🍲 **RIT Boys Hostel Mess Food Directory**\nSelect a day to view Breakfast (7:30 AM), Lunch (12:45 PM), Tea/Snacks (5:15 PM), and Dinner (8:00 PM):",
                "card_kind": "carousel",
                "card_payload": card,
                "agent_used": "MessCanteenAgent",
                "session_updates": {"last_intent": "MESS"}
            }

        # --------------------------------------------------------------------
        # ROUTE 2: CAMPUS CANTEEN MENU
        # --------------------------------------------------------------------
        elif intent == "CANTEEN":
            action = active_context.get("action", "")
            if action == "view_canteen_category" or any(w in query_text.lower() for w in ["burger", "momo", "cold drink", "cold coffee", "coffee", "tea", "fries", "maggi"]):
                res = self.mess_canteen_agent.handle(query_text, active_context)
                card = canteen_category_detail_card(res["category"])
                return {
                    "text": res["text"],
                    "card_kind": "detail",
                    "card_payload": card,
                    "agent_used": "MessCanteenAgent",
                    "session_updates": {"canteen_category": res["category"], "last_intent": "CANTEEN"}
                }

            card = canteen_carousel()
            return {
                "text": "🍔 **Campus Canteen Menu & Fast Food Counter**\nExplore Burgers, Full Plate Momos, Cold Drinks, Hot/Cold Coffee, and Snacks with student prices:",
                "card_kind": "carousel",
                "card_payload": card,
                "agent_used": "MessCanteenAgent",
                "session_updates": {"last_intent": "CANTEEN"}
            }

        # --------------------------------------------------------------------
        # ROUTE 3: TIMETABLES
        # --------------------------------------------------------------------
        elif intent == "TIMETABLE":
            action = active_context.get("action", "")

            if action == "view_timetable" or "day" in active_context or any(d in query_text.lower() for d in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]):
                res = self.timetable_agent.handle(query_text, active_context)
                card = timetable_schedule_detail(res["year_key"], res["day"])
                return {
                    "text": res["text"],
                    "card_kind": "detail",
                    "card_payload": card,
                    "agent_used": "TimetableAgent",
                    "session_updates": {"year": res["year_key"], "last_intent": "TIMETABLE"}
                }

            if action == "select_year":
                year_key = active_context.get("year", "1st_year")
                res = self.timetable_agent.handle("Monday", {"year": year_key})
                card = timetable_schedule_detail(year_key, "Monday")
                return {
                    "text": f"📅 Schedule for **{res['title']} (Monday)**. Click approve to view Tuesday or other days:",
                    "card_kind": "detail",
                    "card_payload": card,
                    "agent_used": "TimetableAgent",
                    "session_updates": {"year": year_key}
                }

            card = timetables_year_carousel()
            return {
                "text": "📅 **Select an Academic Year (RIT Official Timetables)** to view weekly lecture routines, lab venues, and professors:",
                "card_kind": "carousel",
                "card_payload": card,
                "agent_used": "TimetableAgent",
                "session_updates": {"last_intent": "TIMETABLE"}
            }

        # --------------------------------------------------------------------
        # ROUTE 4: CAMPUS BUILDINGS & NAVIGATION
        # --------------------------------------------------------------------
        elif intent == "NAVIGATION":
            action = active_context.get("action", "")

            if action == "view_building" or "bldg_id" in active_context:
                bldg_id = active_context.get("bldg_id", "bldg_block_b")
                res = self.navigation_agent.handle(query_text, {"bldg_id": bldg_id})
                card = building_detail_card(bldg_id)
                return {
                    "text": res["text"],
                    "card_kind": "detail",
                    "card_payload": card,
                    "agent_used": "NavigationAgent",
                    "session_updates": {"bldg_id": bldg_id, "last_intent": "NAVIGATION"}
                }

            res = self.navigation_agent.handle(query_text, active_context)
            if res.get("type") == "building_detail":
                card = building_detail_card(res["building"]["id"])
                kind = "detail"
            else:
                card = buildings_carousel()
                kind = "carousel"

            return {
                "text": res["text"],
                "card_kind": kind,
                "card_payload": card,
                "agent_used": "NavigationAgent",
                "session_updates": {"last_intent": "NAVIGATION"}
            }

        # --------------------------------------------------------------------
        # ROUTE 5: FACULTY DIRECTORY
        # --------------------------------------------------------------------
        elif intent == "FACULTY":
            action = active_context.get("action", "")

            if action == "view_faculty" or "fac_id" in active_context:
                fac_id = active_context.get("fac_id", "fac_dr_lokesh")
                res = self.faculty_agent.handle(query_text, {"fac_id": fac_id})
                card = faculty_detail_card(fac_id)
                return {
                    "text": res["text"],
                    "card_kind": "detail",
                    "card_payload": card,
                    "agent_used": "FacultyAgent",
                    "session_updates": {"fac_id": fac_id, "last_intent": "FACULTY"}
                }

            res = self.faculty_agent.handle(query_text, active_context)
            if res.get("type") == "faculty_detail":
                card = faculty_detail_card(res["faculty"]["id"])
                kind = "detail"
            else:
                card = faculty_carousel()
                kind = "carousel"

            return {
                "text": res["text"],
                "card_kind": kind,
                "card_payload": card,
                "agent_used": "FacultyAgent",
                "session_updates": {"last_intent": "FACULTY"}
            }

        # --------------------------------------------------------------------
        # ROUTE 6: COLLEGE DOCUMENTS RAG
        # --------------------------------------------------------------------
        elif intent == "RAG":
            res = self.rag_agent.handle(query_text, active_context)
            card = rag_result_card(query_text, res.get("hits", []))
            return {
                "text": res["text"],
                "card_kind": "detail",
                "card_payload": card,
                "agent_used": "RAGAgent",
                "session_updates": {"last_intent": "RAG"}
            }

        # --------------------------------------------------------------------
        # DEFAULT: MAIN MENU
        # --------------------------------------------------------------------
        card = main_menu_carousel()
        text = (
            "👋 **Namaste! Welcome to CampusMitra AI (RIT Roorkee Edition).**\n\n"
            "I am your official smart Indian campus concierge. I can assist you with:\n"
            "• 📅 **1st to 4th Year Class Timetables** (Mon - Sat routines, rooms & faculty)\n"
            "• 🍲 **Hostel Mess Food** (Breakfast, Lunch, Tea/Snacks & Dinner for Mon - Sun)\n"
            "• 🍔 **Campus Canteen Menu** (Burgers, Full Plate Momos, Cold Drinks, Cold Coffee)\n"
            "• 🏛️ **Campus Buildings & Floor Classrooms** (Block B, Block C, Block D)\n"
            "• 👨‍🏫 **Faculty Directory & Cabin Locations** (HOD, Professors, Office Hours)\n"
            "• 📖 **Academic Handbook RAG** (75% Attendance rule, Condonation & Exam policies)\n\n"
            "Please choose a service below or type your query directly!"
        )
        return {
            "text": text,
            "card_kind": "carousel",
            "card_payload": card,
            "agent_used": "CampusMitraOrchestrator",
            "session_updates": {"last_intent": "MAIN_MENU"}
        }
