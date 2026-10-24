"""
CampusMitra AI - ASI:One Interactive Cards Protocol Builder
Produces Carousel, Detail, Form, and Review cards for:
- 1st-4th Year Timetables (Roorkee Institute of Technology)
- Boys Hostel Mess Menu (Mon - Sun: Breakfast, Lunch, Snacks, Dinner)
- Campus Canteen Menu (Burgers, Full Plate Momos, Cold Drinks, Cold Coffee, Tea)
- Buildings, Floors & Classrooms (Block B, Block C, Block D)
- Faculty Directory & Cabins
- Handbook RAG Query Citations
"""
import json
from datetime import datetime, timezone
from uuid import uuid4
from uagents_core.contrib.protocols.chat import (
    ChatMessage,
    MetadataContent,
    TextContent,
)

from ..data.campus_data import (
    BUILDINGS,
    FACULTY_MEMBERS,
    TIMETABLES,
    MESS_MENU,
    MESS_TIMINGS,
    CANTEEN_MENU,
    get_building_by_id,
    get_faculty_by_id,
    get_timetable,
    get_mess_menu,
    get_canteen_menu,
    find_room_location,
)


def create_card_msg(narration: str, kind: str, payload: dict, is_terminal: bool = False, drawer_width: str = "540") -> ChatMessage:
    """Wraps text narration + ASI Interactive Card JSON payload in a standard ChatMessage."""
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


# ---------------------------------------------------------------------------
# 1. Main Menu Carousel
# ---------------------------------------------------------------------------
def main_menu_carousel() -> dict:
    return {
        "title": "CampusMitra AI: Smart Campus Concierge",
        "subtitle": "Timetables, Hostel Mess Food, Canteen, Classrooms & Faculty",
        "items": [
            {
                "id": "menu_timetables",
                "image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=600",
                "title": "Class Timetables (1st - 4th Year)",
                "subtitle": "Mon - Sat schedules with rooms & professors",
                "badges": [{"label": "All 4 Years", "variant": "success"}, {"label": "RIT Official", "variant": "info"}],
                "secondary_text": "Live lecture timings, lab venues & faculty",
                "primary_cta": {"label": "Browse Timetables", "selection": {"action": "menu_timetables"}}
            },
            {
                "id": "menu_mess",
                "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600",
                "title": "Hostel Mess Food (Mon - Sun)",
                "subtitle": "Breakfast, Lunch, Tea/Snacks & Dinner",
                "badges": [{"label": "All 7 Days", "variant": "warning"}, {"label": "Boys Mess", "variant": "info"}],
                "secondary_text": "Aloo Paratha, Paneer, Kheer, Chole Bhature, Ice Cream",
                "primary_cta": {"label": "View Mess Menu", "selection": {"action": "menu_mess"}}
            },
            {
                "id": "menu_canteen",
                "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600",
                "title": "Campus Canteen Menu",
                "subtitle": "Burgers, Full Plate Momos, Cold Drinks, Cold Coffee",
                "badges": [{"label": "Canteen", "variant": "success"}, {"label": "Quick Bites", "variant": "info"}],
                "secondary_text": "Burgers, Steamed/Fried Momos, Cold Coffee, Tea & Maggi",
                "primary_cta": {"label": "View Canteen Menu", "selection": {"action": "menu_canteen"}}
            },
            {
                "id": "menu_buildings",
                "image": "https://images.unsplash.com/photo-1562774053-701939374585?w=600",
                "title": "Campus Buildings & Classrooms",
                "subtitle": "Block B, Block C, Block D & Central Library",
                "badges": [{"label": "3 Academic Blocks", "variant": "info"}, {"label": "Floor Maps", "variant": "success"}],
                "secondary_text": "Find room locations (B-001, C-202, C-212, D-202)",
                "primary_cta": {"label": "Explore Buildings", "selection": {"action": "menu_buildings"}}
            },
            {
                "id": "menu_faculty",
                "image": "https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=600",
                "title": "Faculty & Cabin Directory",
                "subtitle": "HOD CSE, Professors, Subjects & Visiting Hours",
                "badges": [{"label": "Faculty Cabins", "variant": "info"}],
                "secondary_text": "Dr. Lokesh Kumar, Dr. Atma Rai, Dr. Himanshu Gupta",
                "primary_cta": {"label": "View Faculty", "selection": {"action": "menu_faculty"}}
            }
        ]
    }


# ---------------------------------------------------------------------------
# 2. Hostel Mess Cards
# ---------------------------------------------------------------------------
def mess_days_carousel() -> dict:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_highlights = {
        "Monday": "Breakfast: Aloo Paratha, Dahi · Dinner: Shahi Paneer & Kheer",
        "Tuesday": "Breakfast: Pav Bhaji · Dinner: Dal Arhar & Hot Jalebi",
        "Wednesday": "Breakfast: Aloo Puri · Lunch: Kadai Paneer · Dinner: Sewaiya",
        "Thursday": "Breakfast: Onion Paratha · Tea: Finger Chips · Dinner: Gulab Jamun",
        "Friday": "Breakfast: Idli Sambhar / Daliya · Dinner: Manchurian & Custard",
        "Saturday": "Breakfast: Palak Paratha · Tea: Samosa · Dinner: Suji Halwa",
        "Sunday": "Breakfast: Chole Bhature · Lunch: Veg Biryani · Dinner: Ice Cream"
    }

    return {
        "title": "RIT Boys Hostel Mess - Select Day",
        "subtitle": "Full day food: Breakfast (7:30 AM), Lunch (12:45 PM), Tea (5:15 PM), Dinner (8:00 PM)",
        "items": [
            {
                "id": f"mess_{d.lower()}",
                "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600",
                "title": f"{d} Mess Food",
                "subtitle": "Breakfast, Lunch, Snacks & Dinner",
                "badges": [{"label": "4 Meals", "variant": "success"}, {"label": d, "variant": "info"}],
                "secondary_text": day_highlights[d],
                "primary_cta": {"label": f"View {d} Menu", "selection": {"action": "view_mess", "day": d}}
            }
            for d in days
        ]
    }


def mess_detail_card(day: str = "Monday") -> dict:
    data = get_mess_menu(day)
    meals = data["meals"]
    timings = data["timings"]

    rows = [
        {"label": f"🍳 Breakfast ({timings['breakfast']})", "value": meals["breakfast"]},
        {"label": f"🍛 Lunch ({timings['lunch']})", "value": meals["lunch"]},
        {"label": f"☕ Tea & Snacks ({timings['tea_snacks']})", "value": meals["tea_snacks"]},
        {"label": f"🍲 Dinner ({timings['dinner']})", "value": meals["dinner"]}
    ]

    next_days = {
        "Monday": "Tuesday", "Tuesday": "Wednesday", "Wednesday": "Thursday",
        "Thursday": "Friday", "Friday": "Saturday", "Saturday": "Sunday", "Sunday": "Monday"
    }
    next_day = next_days.get(data["day"], "Monday")

    return {
        "title": f"RIT Hostel Mess Menu: {data['day']}",
        "hero_image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600",
        "summary_rows": rows,
        "approve_cta": {
            "label": f"View {next_day}'s Food",
            "primary": True,
            "selection": {"action": "view_mess", "day": next_day}
        },
        "reject_cta": {
            "label": "All Days Menu",
            "selection": {"action": "menu_mess"}
        }
    }


# ---------------------------------------------------------------------------
# 3. Canteen Menu Cards
# ---------------------------------------------------------------------------
def canteen_carousel() -> dict:
    categories = list(CANTEEN_MENU.keys())
    cat_images = {
        "Burgers": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600",
        "Momos (Full Plate - 8 Pieces)": "https://images.unsplash.com/photo-1625246333195-78d9c38ad449?w=600",
        "Cold Drinks & Chilled Beverages": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=600",
        "Coffee & Hot Beverages": "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?w=600",
        "Cold Coffee & Shakes": "https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5?w=600",
        "Snacks & Quick Bites": "https://images.unsplash.com/photo-1576107232684-1279f3908594?w=600"
    }

    return {
        "title": "Campus Canteen Menu",
        "subtitle": "Burgers, Full Plate Momos, Cold Drinks, Hot/Cold Coffee & Snacks",
        "items": [
            {
                "id": f"canteen_{cat.split()[0].lower()}",
                "image": cat_images.get(cat, "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600"),
                "title": cat,
                "subtitle": f"{len(CANTEEN_MENU[cat])} Items Available",
                "badges": [{"label": "Canteen", "variant": "success"}],
                "secondary_text": ", ".join([item["name"] for item in CANTEEN_MENU[cat][:3]]),
                "primary_cta": {"label": f"View {cat.split()[0]} Items", "selection": {"action": "view_canteen_category", "category": cat}}
            }
            for cat in categories
        ]
    }


def canteen_category_detail_card(category: str) -> dict:
    items = CANTEEN_MENU.get(category, CANTEEN_MENU["Burgers"])
    rows = []
    for it in items:
        rows.append({
            "label": f"{it['name']} ({it['price']})",
            "value": it["desc"]
        })

    return {
        "title": f"Canteen: {category}",
        "hero_image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600",
        "summary_rows": rows,
        "approve_cta": {
            "label": "Explore Other Categories",
            "primary": True,
            "selection": {"action": "menu_canteen"}
        },
        "reject_cta": {
            "label": "Main Menu",
            "selection": {"action": "main_menu"}
        }
    }


# ---------------------------------------------------------------------------
# 4. Timetable Cards
# ---------------------------------------------------------------------------
def timetables_year_carousel() -> dict:
    return {
        "title": "Select Academic Year (RIT Official Timetables)",
        "subtitle": "Schedules with subjects, timings, room numbers and faculty",
        "items": [
            {
                "id": "1st_year",
                "image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=600",
                "title": "1st Year (B.Tech CSE Sec A)",
                "subtitle": "Venue: Block B, Room B-001",
                "badges": [{"label": "Room B-001", "variant": "info"}],
                "secondary_text": "Engineering Maths, Programming in C, Physics, Electrical",
                "primary_cta": {"label": "View 1st Year Schedule", "selection": {"action": "select_year", "year": "1st_year"}}
            },
            {
                "id": "2nd_year",
                "image": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600",
                "title": "2nd Year (B.Tech CSE Sec IIA-A)",
                "subtitle": "Venue: Block C, Room C-202",
                "badges": [{"label": "Room C-202", "variant": "success"}],
                "secondary_text": "DSA, OOPs Java, Python, Discrete Maths, IBM Training, GFG",
                "primary_cta": {"label": "View 2nd Year Schedule", "selection": {"action": "select_year", "year": "2nd_year"}}
            },
            {
                "id": "3rd_year",
                "image": "https://images.unsplash.com/photo-1531482615713-2afd69097998?w=600",
                "title": "3rd Year (B.Tech CSE Sec IIIA-A)",
                "subtitle": "Venue: Block C, Room C-212",
                "badges": [{"label": "Room C-212", "variant": "warning"}],
                "secondary_text": "Compiler Design, DBMS, DAA, Distributed Systems, Software Engg",
                "primary_cta": {"label": "View 3rd Year Schedule", "selection": {"action": "select_year", "year": "3rd_year"}}
            },
            {
                "id": "4th_year",
                "image": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600",
                "title": "4th Year (B.Tech Final Year)",
                "subtitle": "Venue: Block D, Room D-202",
                "badges": [{"label": "Room D-202", "variant": "danger"}],
                "secondary_text": "Cloud Computing, Machine Learning, Mobile Tech, Capstone Project",
                "primary_cta": {"label": "View 4th Year Schedule", "selection": {"action": "select_year", "year": "4th_year"}}
            }
        ]
    }


def timetable_schedule_detail(year_key: str, day: str = "Monday") -> dict:
    tt = get_timetable(year_key, day)
    rows = [
        {"label": "Classroom", "value": tt["classroom"]},
        {"label": "Day", "value": tt["day"]}
    ]
    for slot in tt["schedule"]:
        rows.append({
            "label": slot["time"],
            "value": f"{slot['subject']} | Room: {slot['room']} ({slot['faculty']})"
        })

    next_days = {"Monday": "Tuesday", "Tuesday": "Wednesday", "Wednesday": "Thursday", "Thursday": "Friday", "Friday": "Saturday", "Saturday": "Monday"}
    next_day = next_days.get(tt["day"], "Monday")

    return {
        "title": f"Schedule: {tt['title']} ({tt['day']})",
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


# ---------------------------------------------------------------------------
# 5. Buildings & Classrooms Cards
# ---------------------------------------------------------------------------
def buildings_carousel() -> dict:
    return {
        "title": "RIT Campus Buildings & Classrooms",
        "subtitle": "Click any building to inspect floor-by-floor classroom and lab allocations",
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


def building_detail_card(bldg_id: str) -> dict:
    b = get_building_by_id(bldg_id) or BUILDINGS["bldg_block_b"]
    rows = [
        {"label": "Building Code", "value": b["code"]},
        {"label": "Total Floors", "value": f"{b['total_floors']} Floors"},
        {"label": "Overview", "value": b["description"]}
    ]
    for floor, rooms in b["floors"].items():
        room_strs = [f"{r['room']} ({r['name']})" for r in rooms]
        rows.append({
            "label": floor,
            "value": " • ".join(room_strs)
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


# ---------------------------------------------------------------------------
# 6. Faculty Cards
# ---------------------------------------------------------------------------
def faculty_carousel() -> dict:
    return {
        "title": "Faculty Directory & Cabins (RIT)",
        "subtitle": "Explore professors, department designations, subjects, and visiting hours",
        "items": [
            {
                "id": f["id"],
                "image": f["avatar"],
                "title": f["name"],
                "subtitle": f"{f['designation']} · {f['department']}",
                "badges": [
                    {"label": f["cabin"].split(',')[0], "variant": "info"},
                    {"label": f["subjects"][0].split('(')[0].strip(), "variant": "success"}
                ],
                "secondary_text": f"Visiting: {f['office_hours']}",
                "primary_cta": {
                    "label": "View Cabin & Profile",
                    "selection": {"action": "view_faculty", "fac_id": f["id"]}
                }
            }
            for f in FACULTY_MEMBERS
        ]
    }


def faculty_detail_card(fac_id: str) -> dict:
    f = get_faculty_by_id(fac_id) or FACULTY_MEMBERS[0]
    return {
        "title": f["name"],
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
            "label": "Browse All Faculty",
            "primary": True,
            "selection": {"action": "menu_faculty"}
        },
        "reject_cta": {
            "label": "Main Menu",
            "selection": {"action": "main_menu"}
        }
    }


# ---------------------------------------------------------------------------
# 7. RAG Result Card
# ---------------------------------------------------------------------------
def rag_result_card(query: str, hits: list) -> dict:
    rows = [{"label": "Handbook Query", "value": query}]
    for idx, hit in enumerate(hits, 1):
        excerpt = hit["text"][:140] + ("..." if len(hit["text"]) > 140 else "")
        rows.append({
            "label": f"Page {hit.get('page', 1)} Match #{idx}",
            "value": excerpt
        })

    return {
        "title": "RIT Handbook RAG Findings",
        "hero_image": "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=600",
        "summary_rows": rows,
        "approve_cta": {
            "label": "Ask Another Regulation Query",
            "primary": True,
            "selection": {"action": "menu_rag"}
        },
        "reject_cta": {
            "label": "Main Menu",
            "selection": {"action": "main_menu"}
        }
    }
