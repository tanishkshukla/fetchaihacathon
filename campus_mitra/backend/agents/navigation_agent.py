"""
CampusMitra AI - Navigation & Campus Infrastructure Agent
Locates buildings, floor-by-floor maps, classrooms, labs, and directions.
"""
from typing import Dict, Any, Optional
from ..data.campus_data import BUILDINGS, get_building_by_id, find_room_location


class NavigationAgent:
    def __init__(self):
        self.name = "NavigationAgent"

    def handle(self, query: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        q = query.lower()
        context = context or {}

        # 1. Check if building ID is in context or query
        bldg = None
        for b_id, b_data in BUILDINGS.items():
            if b_id in q or b_data["code"].lower() in q or b_data["name"].lower() in q:
                bldg = b_data
                break
        if not bldg and "bldg_id" in context:
            bldg = get_building_by_id(context["bldg_id"])

        if bldg:
            floor_texts = []
            for fl, rooms in bldg["floors"].items():
                r_str = ", ".join([f"{r['room']} ({r['name']})" for r in rooms])
                floor_texts.append(f"• **{fl}**: {r_str}")
            
            floor_summary = "\n".join(floor_texts)
            text = (
                f"🏛️ **{bldg['name']} ({bldg['code']})**\n"
                f"• **Total Floors**: {bldg['total_floors']}\n"
                f"• **Overview**: {bldg['description']}\n\n"
                f"**Floor Directory**:\n{floor_summary}"
            )
            return {
                "agent": self.name,
                "type": "building_detail",
                "building": bldg,
                "text": text
            }

        # 2. Check for room / lab search
        matches = find_room_location(q)
        if matches:
            top = matches[0]
            other_lines = [
                f"• `{m['room_code']}` ({m['room_name']}): {m['building_name']} - **{m['floor']}**"
                for m in matches
            ]
            text = (
                f"📍 **Found Location for `{top['room_code']}` ({top['room_name']})**\n\n"
                f"• **Building**: {top['building_name']} (`{top['building_code']}`)\n"
                f"• **Floor**: {top['floor']}\n"
                f"• **Type**: {top['room_type']}\n\n"
                f"**Matching facilities**:\n" + "\n".join(other_lines)
            )
            return {
                "agent": self.name,
                "type": "room_search",
                "matches": matches,
                "text": text
            }

        # 3. Default: List all 4 campus complexes
        bldg_list = [f"• **{b['name']}** (`{b['code']}`): {b['total_floors']} floors - {b['description']}" for b in BUILDINGS.values()]
        text = "🏛️ **Campus Buildings & Infrastructure**\n\n" + "\n".join(bldg_list)
        return {
            "agent": self.name,
            "type": "buildings_list",
            "buildings": list(BUILDINGS.values()),
            "text": text
        }
