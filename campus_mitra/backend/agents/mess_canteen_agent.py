"""
CampusMitra AI - Mess & Canteen Specialist Agent
Processes queries related to Boys Hostel Mess food (Breakfast, Lunch, Snacks, Dinner)
and Campus Canteen orders (Burgers, Full Plate Momos, Cold Drinks, Cold Coffee, Tea).
"""
from typing import Dict, Any, Optional
from ..data.campus_data import get_mess_menu, get_canteen_menu, MESS_TIMINGS, MESS_MENU, CANTEEN_MENU


class MessCanteenAgent:
    def __init__(self):
        self.name = "MessCanteenAgent"

    def handle(self, query: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        q = query.lower()
        context = context or {}

        # -------------------------------------------------------------
        # CANTEEN QUERIES
        # -------------------------------------------------------------
        if any(w in q for w in ["canteen", "burger", "momo", "cold drink", "cold coffee", "coffee", "tea", "fries", "maggi", "sandwich", "price", "menu"]):
            category = "Burgers"
            if "momo" in q:
                category = "Momos (Full Plate - 8 Pieces)"
            elif any(w in q for w in ["cold drink", "coke", "thums up", "sprite", "mountain dew", "frooti"]):
                category = "Cold Drinks & Chilled Beverages"
            elif "cold coffee" in q or "shake" in q or "frappe" in q:
                category = "Cold Coffee & Shakes"
            elif any(w in q for w in ["tea", "chai", "hot coffee"]):
                category = "Coffee & Hot Beverages"
            elif any(w in q for w in ["fries", "maggi", "sandwich"]):
                category = "Snacks & Quick Bites"
            elif "category" in context:
                category = context["category"]

            items = CANTEEN_MENU.get(category, CANTEEN_MENU["Burgers"])
            item_lines = [f"• **{it['name']}** — `{it['price']}` ({it['desc']})" for it in items]

            text = (
                f"🍔 **Campus Canteen Menu: {category}**\n\n"
                + "\n".join(item_lines) +
                "\n\n*Available daily at the Campus Canteen (1st Floor, Amenities Complex).*"
            )
            return {
                "agent": self.name,
                "type": "canteen",
                "category": category,
                "items": items,
                "text": text
            }

        # -------------------------------------------------------------
        # MESS FOOD QUERIES
        # -------------------------------------------------------------
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        selected_day = "Monday"
        for d in days:
            if d in q:
                selected_day = d.capitalize()
                break
        if "day" in context and not any(d in q for d in days):
            selected_day = context["day"].capitalize()

        mess_data = get_mess_menu(selected_day)
        meals = mess_data["meals"]
        timings = mess_data["timings"]

        # Check if user asked about a specific meal
        specific_meal = None
        if "breakfast" in q: specific_meal = "breakfast"
        elif "lunch" in q: specific_meal = "lunch"
        elif any(w in q for w in ["tea", "snack"]): specific_meal = "tea_snacks"
        elif "dinner" in q: specific_meal = "dinner"

        if specific_meal:
            meal_names = {
                "breakfast": "🍳 Breakfast",
                "lunch": "🍛 Lunch",
                "tea_snacks": "☕ Tea & Snacks",
                "dinner": "🍲 Dinner"
            }
            text = (
                f"🍲 **RIT Hostel Mess - {selected_day} {meal_names[specific_meal]} ({timings[specific_meal]})**\n\n"
                f"• {meals[specific_meal]}"
            )
        else:
            text = (
                f"🍲 **RIT Hostel Mess Menu for {selected_day}**\n\n"
                f"• **🍳 Breakfast ({timings['breakfast']})**:\n  {meals['breakfast']}\n\n"
                f"• **🍛 Lunch ({timings['lunch']})**:\n  {meals['lunch']}\n\n"
                f"• **☕ Tea & Snacks ({timings['tea_snacks']})**:\n  {meals['tea_snacks']}\n\n"
                f"• **🍲 Dinner ({timings['dinner']})**:\n  {meals['dinner']}"
            )

        return {
            "agent": self.name,
            "type": "mess",
            "day": selected_day,
            "meals": meals,
            "text": text
        }
