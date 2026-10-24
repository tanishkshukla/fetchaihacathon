"""
CampusMitra AI - ASI:One Interactive Cards Protocol
Generates Carousel, Detail, Form, and Review cards for campus navigation,
timetables for 1st-4th year, buildings & classrooms, and faculty directory.
"""

import json
from datetime import datetime, timezone
from uuid import uuid4
from uagents_core.contrib.protocols.chat import (
    ChatMessage,
    MetadataContent,
    TextContent,
)

from campus_data import BUILDINGS, FACULTY_MEMBERS, TIMETABLES, get_timetable, get_building_by_id, get_faculty_by_id, find_room_location


def card_msg(narration: str, kind: str, payload: dict, is_terminal: bool = False, drawer_width: str = "540") -> ChatMessage:
    """Helper to package text narration + ASI Interactive Card metadata."""
    return ChatMessage(
        timestamp=datetime.now(timezone.utc),
        msg_id=uuid4(),
        content=[
            TextContent(type="text", text=narration),
            MetadataContent(
                type="metadata",
                metadata={
                    "card_protocol_version": "1",
                    "requires_card_interaction": "false" if is_terminal else "true",
                    "card_kind": kind,
                    "card_payload": json.dumps(payload),
                    "preferred_drawer_width_px": drawer_width,
                },
            ),
        ],
    )


# ============================================================================
# 1. MAIN MENU CAROUSEL
# ============================================================================
def main_menu_carousel_payload() -> dict:
    return {
        "title": "CampusMitra AI: Smart Campus Concierge",
        "subtitle": "Instant access to timetables, classrooms, faculty cabins, and building navigation",
        "items": [
            {
                "id": "menu_timetables",
                "image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=600",
                "title": "Class Timetables (1st - 4th Year)",
                "subtitle": "B.Tech Foundation, CSE Core, Specialization & Labs",
                "badges": [
                    {"label": "All 4 Years", "variant": "success"},
                    {"label": "Mon - Fri", "variant": "info"}
                ],
                "secondary_text": "Live schedules with subject, timing, faculty, and room numbers",
                "primary_cta": {
                    "label": "Explore Timetables",
                    "selection": {"action": "menu_timetables"}
                }
            },
            {
                "id": "menu_buildings",
                "image": "https://images.unsplash.com/photo-1562774053-701939374585?w=600",
                "title": "Campus Buildings & Classrooms",
                "subtitle": "Turing CS Block, Ramanujan Block, ECE Block, Central Library",
                "badges": [
                    {"label": "4 Buildings", "variant": "success"},
                    {"label": "Floor Maps", "variant": "info"}
                ],
                "secondary_text": "Detailed floor-by-floor breakdown of lecture halls & labs",
                "primary_cta": {
                    "label": "View Buildings",
                    "selection": {"action": "menu_buildings"}
                }
            },
            {
                "id": "menu_faculty",
                "image": "https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=600",
                "title": "Faculty & Cabin Directory",
                "subtitle": "Professors, Subjects Taught, Cabin Numbers & Office Hours",
                "badges": [
                    {"label": "Professors", "variant": "info"},
                    {"label": "Office Hours", "variant": "warning"}
                ],
                "secondary_text": "Connect with faculty and find their exact cabin locations",
                "primary_cta": {
                    "label": "View Faculty Directory",
                    "selection": {"action": "menu_faculty"}
                }
            },
            {
                "id": "menu_locator",
                "image": "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=600",
                "title": "Quick Room & Lab Locator",
                "subtitle": "Find any Classroom, Lecture Theater, or Computing Lab",
                "badges": [
                    {"label": "Search Any Room", "variant": "info"}
                ],
                "secondary_text": "Enter room number (e.g. CS-201, LT-1, AI Lab) for direct directions",
                "primary_cta": {
                    "label": "Locate a Room",
                    "selection": {"action": "menu_locator"}
                }
            }
        ]
    }


# ============================================================================
# 2. TIMETABLE CARDS
# ============================================================================
def timetables_year_carousel_payload() -> dict:
    return {
        "title": "Select Academic Year",
        "subtitle": "Choose your year to check day-wise class schedule and room allocations",
        "items": [
            {
                "id": "1st_year",
                "image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=600",
                "title": "1st Year (Foundation)",
                "subtitle": "B.Tech Common First Year",
                "badges": [{"label": "Ramanujan LT-1", "variant": "info"}],
                "secondary_text": "Subjects: Engg Maths, Physics, C Programming, Electrical Engg",
                "primary_cta": {
                    "label": "View 1st Year Schedule",
                    "selection": {"action": "select_year", "year": "1st_year"}
                }
            },
            {
                "id": "2nd_year",
                "image": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600",
                "title": "2nd Year (Sophomore)",
                "subtitle": "Computer Science & Engineering",
                "badges": [{"label": "Turing CS-201", "variant": "success"}],
                "secondary_text": "Subjects: Data Structures, OOPs Java, Discrete Maths, COA",
                "primary_cta": {
                    "label": "View 2nd Year Schedule",
                    "selection": {"action": "select_year", "year": "2nd_year"}
                }
            },
            {
                "id": "3rd_year",
                "image": "https://images.unsplash.com/photo-1531482615713-2afd69097998?w=600",
                "title": "3rd Year (Junior)",
                "subtitle": "Computer Science & Engineering",
                "badges": [{"label": "Turing CS-301", "variant": "warning"}],
                "secondary_text": "Subjects: Operating Systems, DBMS, Machine Learning, Networks",
                "primary_cta": {
                    "label": "View 3rd Year Schedule",
                    "selection": {"action": "select_year", "year": "3rd_year"}
                }
            },
            {
                "id": "4th_year",
                "image": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600",
                "title": "4th Year (Final Year)",
                "subtitle": "B.Tech CSE Specialization & Capstone",
                "badges": [{"label": "Turing CS-401", "variant": "danger"}],
                "secondary_text": "Subjects: Distributed Systems, Deep Learning, Cybersecurity, Major Project",
                "primary_cta": {
                    "label": "View 4th Year Schedule",
                    "selection": {"action": "select_year", "year": "4th_year"}
                }
            }
        ]
    }


def timetable_day_form_payload(year_key: str) -> dict:
    year_data = TIMETABLES.get(year_key, TIMETABLES["1st_year"])
    return {
        "title": f"Select Day: {year_data['title']}",
        "subtitle": f"Primary Classroom: {year_data['classroom']}",
        "fields": [
            {
                "name": "day",
                "kind": "select",
                "label": "Day of the Week",
                "options": [
                    {"value": "Monday", "label": "Monday"},
                    {"value": "Tuesday", "label": "Tuesday"},
                    {"value": "Wednesday", "label": "Wednesday"},
                    {"value": "Thursday", "label": "Thursday"},
                    {"value": "Friday", "label": "Friday"}
                ],
                "required": True
            }
        ],
        "submit_cta": {
            "label": "Show Timetable",
            "selection": {"action": "view_timetable", "year": year_key}
        }
    }


def timetable_schedule_detail_payload(year_key: str, day: str = "Monday") -> dict:
    tt = get_timetable(year_key, day)
    
    rows = [
        {"label": "Classroom", "value": tt["classroom"]},
        {"label": "Day", "value": tt["day"]}
    ]
    for slot in tt["schedule"]:
        rows.append({
            "label": slot["time"],
            "value": f"{slot['subject']} | {slot['room']} ({slot['faculty']})"
        })

    next_days = {
        "Monday": "Tuesday",
        "Tuesday": "Wednesday",
        "Wednesday": "Thursday",
        "Thursday": "Friday",
        "Friday": "Monday"
    }
    next_day = next_days.get(tt["day"], "Monday")

    return {
        "title": f"Timetable: {tt['title']} ({tt['day']})",
        "hero_image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=600",
        "summary_rows": rows,
        "approve_cta": {
            "label": f"View {next_day}'s Schedule",
            "primary": True,
            "selection": {"action": "view_timetable", "year": year_key, "day": next_day}
        },
        "reject_cta": {
            "label": "Change Year",
            "selection": {"action": "menu_timetables"}
        }
    }


# ============================================================================
# 3. BUILDINGS & CLASSROOM CARDS
# ============================================================================
def buildings_carousel_payload() -> dict:
    return {
        "title": "Campus Buildings & Infrastructure",
        "subtitle": "Select a building to view floor layout, classrooms, and lab locations",
        "items": [
            {
                "id": b["id"],
                "image": b["icon_url"],
                "title": b["name"],
                "subtitle": f"{b['code']} · {b['total_floors']} Floors",
                "badges": [{"label": f"{b['total_floors']} Floors", "variant": "info"}],
                "secondary_text": b["description"],
                "primary_cta": {
                    "label": "View Floor Map & Rooms",
                    "selection": {"action": "view_building", "bldg_id": b["id"]}
                }
            }
            for b in BUILDINGS.values()
        ]
    }


def building_detail_payload(bldg_id: str) -> dict:
    b = get_building_by_id(bldg_id) or BUILDINGS["bldg_turing"]
    
    rows = [
        {"label": "Building Code", "value": b["code"]},
        {"label": "Total Floors", "value": f"{b['total_floors']} Floors"},
        {"label": "Overview", "value": b["description"]}
    ]
    for floor, rooms in b["floors"].items():
        rows.append({
            "label": floor,
            "value": " • ".join(rooms)
        })

    return {
        "title": b["name"],
        "hero_image": b["icon_url"],
        "summary_rows": rows,
        "approve_cta": {
            "label": "Explore Other Buildings",
            "primary": True,
            "selection": {"action": "menu_buildings"}
        },
        "reject_cta": {
            "label": "Main Menu",
            "selection": {"action": "main_menu"}
        }
    }


# ============================================================================
# 4. FACULTY DIRECTORY CARDS
# ============================================================================
def faculty_carousel_payload() -> dict:
    return {
        "title": "Faculty Directory & Cabins",
        "subtitle": "Find professors, subjects taught, cabin numbers, and office visiting hours",
        "items": [
            {
                "id": f["id"],
                "image": f["avatar"],
                "title": f["name"],
                "subtitle": f"{f['designation']} · {f['department']}",
                "badges": [
                    {"label": f["cabin"].split(',')[0], "variant": "info"},
                    {"label": f["subjects"][0], "variant": "success"}
                ],
                "secondary_text": f"Office Hours: {f['office_hours']}",
                "primary_cta": {
                    "label": "View Faculty Profile & Cabin",
                    "selection": {"action": "view_faculty", "fac_id": f["id"]}
                }
            }
            for f in FACULTY_MEMBERS
        ]
    }


def faculty_detail_payload(fac_id: str) -> dict:
    f = get_faculty_by_id(fac_id) or FACULTY_MEMBERS[0]
    return {
        "title": f"{f['name']}",
        "hero_image": f["avatar"],
        "summary_rows": [
            {"label": "Designation", "value": f["designation"]},
            {"label": "Department", "value": f["department"]},
            {"label": "Subjects Taught", "value": ", ".join(f["subjects"])},
            {"label": "Cabin Location", "value": f["cabin"]},
            {"label": "Office Visiting Hours", "value": f["office_hours"]},
            {"label": "Email", "value": f["email"]}
        ],
        "approve_cta": {
            "label": "Back to Faculty List",
            "primary": True,
            "selection": {"action": "menu_faculty"}
        },
        "reject_cta": {
            "label": "Main Menu",
            "selection": {"action": "main_menu"}
        }
    }


# ============================================================================
# 5. ROOM LOCATOR FORM & RESULT CARDS
# ============================================================================
def room_locator_form_payload() -> dict:
    return {
        "title": "Classroom & Lab Finder",
        "subtitle": "Search for any classroom, lecture hall, lab, or office across campus",
        "fields": [
            {
                "name": "room_query",
                "kind": "text",
                "label": "Room / Lab Name or Number",
                "placeholder": "e.g. CS-201, LT-1, AI Lab, Drawing Hall, Library",
                "required": True
            }
        ],
        "submit_cta": {
            "label": "Find Room Location",
            "selection": {"action": "search_room"}
        }
    }


def room_result_detail_payload(query: str, matches: list) -> dict:
    if not matches:
        return {
            "title": f"No matches found for '{query}'",
            "summary_rows": [
                {"label": "Search Query", "value": query},
                {"label": "Suggestion", "value": "Try searching for CS-101, CS-201, CS-301, CS-401, LT-1, EC-101, AI Lab, or Library."}
            ],
            "approve_cta": {
                "label": "Try Another Search",
                "primary": True,
                "selection": {"action": "menu_locator"}
            },
            "reject_cta": {
                "label": "Main Menu",
                "selection": {"action": "main_menu"}
            }
        }

    rows = [{"label": "Search Term", "value": query}]
    for m in matches:
        rows.append({
            "label": m["room"],
            "value": f"{m['building_name']} ({m['building_code']}) - {m['floor']}"
        })

    return {
        "title": f"Location Result: {matches[0]['room']}",
        "hero_image": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=600",
        "summary_rows": rows,
        "approve_cta": {
            "label": f"View {matches[0]['building_code']} Map",
            "primary": True,
            "selection": {"action": "view_building", "bldg_id": matches[0]["building_id"]}
        },
        "reject_cta": {
            "label": "Main Menu",
            "selection": {"action": "main_menu"}
        }
    }
