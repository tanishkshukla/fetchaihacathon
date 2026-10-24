"""
CampusMitra AI - Timetable Specialist Agent
Processes queries related to schedules, class timings, subjects, rooms, and professors
across all 4 years (1st, 2nd, 3rd, 4th Year) for Monday through Friday.
"""
from typing import Dict, Any, Optional
from ..data.campus_data import TIMETABLES, get_timetable


class TimetableAgent:
    def __init__(self):
        self.name = "TimetableAgent"

    def handle(self, query: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Interprets the timetable query and returns structured timetable details.
        """
        q = query.lower()
        context = context or {}

        # 1. Detect Year
        year_key = "1st_year"
        if "2nd" in q or "second" in q or "sophomore" in q:
            year_key = "2nd_year"
        elif "3rd" in q or "third" in q or "junior" in q:
            year_key = "3rd_year"
        elif "4th" in q or "fourth" in q or "final" in q or "senior" in q:
            year_key = "4th_year"
        elif "1st" in q or "first" in q or "foundation" in q:
            year_key = "1st_year"
        elif "year" in context:
            year_key = context["year"]

        # 2. Detect Day
        days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
        selected_day = "Monday"
        for d in days:
            if d in q:
                selected_day = d.capitalize()
                break
        if "day" in context and not any(d in q for d in days):
            selected_day = context["day"].capitalize()

        tt_data = get_timetable(year_key, selected_day)

        # Build natural text summary
        schedule_lines = []
        for slot in tt_data["schedule"]:
            schedule_lines.append(f"• **{slot['time']}**: {slot['subject']} in `{slot['room']}` ({slot['faculty']})")

        schedule_text = "\n".join(schedule_lines)
        response_text = (
            f"📅 **{tt_data['title']} - {tt_data['day']} Schedule**\n"
            f"📍 **Base Classroom**: `{tt_data['classroom']}`\n\n"
            f"{schedule_text}"
        )

        return {
            "agent": self.name,
            "year_key": year_key,
            "day": selected_day,
            "title": tt_data["title"],
            "classroom": tt_data["classroom"],
            "schedule": tt_data["schedule"],
            "text": response_text
        }
