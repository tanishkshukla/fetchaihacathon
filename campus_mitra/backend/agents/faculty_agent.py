"""
CampusMitra AI - Faculty Directory Specialist Agent
Finds professors, designations, subjects taught, cabin locations, and office visiting hours.
"""
from typing import Dict, Any, Optional
from ..data.campus_data import FACULTY_MEMBERS, get_faculty_by_id, search_faculty


class FacultyAgent:
    def __init__(self):
        self.name = "FacultyAgent"

    def handle(self, query: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        q = query.lower()
        context = context or {}

        # 1. Check if specific faculty ID in context or query
        fac = None
        if "fac_id" in context:
            fac = get_faculty_by_id(context["fac_id"])
        
        if not fac:
            matches = search_faculty(q)
            if matches:
                fac = matches[0]

        if fac:
            text = (
                f"👨‍🏫 **{fac['name']}**\n"
                f"• **Designation**: {fac['designation']}\n"
                f"• **Department**: {fac['department']}\n"
                f"• **Subjects Taught**: {', '.join(fac['subjects'])}\n"
                f"• **Cabin Location**: `{fac['cabin']}`\n"
                f"• **Visiting Hours**: {fac['office_hours']}\n"
                f"• **Email**: `{fac['email']}`"
            )
            return {
                "agent": self.name,
                "type": "faculty_detail",
                "faculty": fac,
                "text": text
            }

        # Default: list all faculty
        fac_lines = [
            f"• **{f['name']}** ({f['designation']}) - Cabin: `{f['cabin']}` | Subjects: {', '.join(f['subjects'])}"
            for f in FACULTY_MEMBERS
        ]
        text = "👨‍🏫 **Campus Faculty Directory**\n\n" + "\n".join(fac_lines)
        return {
            "agent": self.name,
            "type": "faculty_list",
            "faculty_list": FACULTY_MEMBERS,
            "text": text
        }
