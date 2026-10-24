"""
CampusMitra AI - All-in-One Agentverse Cloud Hosted Agent (RIT Edition)
Paste this file directly into the Agentverse Web Code Editor (https://agentverse.ai)
to deploy CampusMitra AI 24/7 in the cloud with full ASI:One Interactive Cards support!

Features included:
1. Official Class Timetables: 1st, 2nd, 3rd, and 4th Year (Monday to Saturday, all slots with rooms & faculty)
2. Boys Hostel Mess Menu: Monday to Sunday (Breakfast, Lunch, Tea & Snacks, Dinner)
3. Campus Canteen Menu: Burgers, Full Plate Momos, Cold Drinks, Coffee/Tea, Cold Coffee, Snacks
4. Campus Buildings & Classroom Floor Map: Block B, Block C, Block D, and Central Amenities Complex
5. Faculty Directory & Cabins: HOD CSE, Professors, Subjects, Cabins & Visiting Hours
6. Full ASI:One Interactive Cards: Carousel Cards, Detail Cards, Navigation CTAs
"""
import json
import logging
from datetime import datetime, timezone
from uuid import uuid4

from uagents import Agent, Context, Protocol
from uagents_core.contrib.protocols.chat import (
    ChatAcknowledgement,
    ChatMessage,
    MetadataContent,
    TextContent,
    chat_protocol_spec,
)

# ============================================================================
# 1. MESS MENU & TIMINGS (ALL 7 DAYS - BREAKFAST, LUNCH, SNACKS, DINNER)
# ============================================================================
MESS_TIMINGS = {
    "breakfast": "07:30 AM - 08:30 AM",
    "lunch": "12:45 PM - 01:45 PM",
    "tea_snacks": "05:15 PM - 06:00 PM",
    "dinner": "08:00 PM - 09:00 PM"
}

MESS_MENU = {
    "Monday": {
        "breakfast": "Aloo Paratha, Fresh Dahi, Green Chutney, Amul Packed Butter, Mixed Pickle, Special Chai, Fresh Fruits (Banana)",
        "lunch": "Dal Arhar, Bhindi Masala / Aloo Gobhi, Steamed Basmati Rice, Hot Chapati, Green Salad, Mixed Pickle, Fried Crispy Papad",
        "tea_snacks": "Hot Bread Pakoda, Fresh Mint Chutney, Tomato Ketchup, Masala Tea",
        "dinner": "Dal Urad Channa, Shahi Paneer, Steamed Rice, Butter Chapati, Fresh Green Salad, Pickle, Sweet Dish (Special Kheer)"
    },
    "Tuesday": {
        "breakfast": "Spicy Mumbai Pav Bhaji with Chopped Onions & Lemon, Fresh Apple, Hot Milk / Tea",
        "lunch": "Peas Pulao Rice, Punjabi Rajma Masala, Tangy Chutney, Dahi Bhalla, Hot Chapati, Green Salad, Pickle, Fried Papad",
        "tea_snacks": "Mix Veg Hakka Noodles, Tomato Ketchup, Hot Tea",
        "dinner": "Dal Arhar Tadka, Seasonal Mix Veg, Steamed Rice, Hot Chapati, Salad, Mixed Pickle, Sweet Dish (Hot Jalebi)"
    },
    "Wednesday": {
        "breakfast": "Crispy Puri with Spicy Aloo Ki Sabji, Pickles, Hot Filter Coffee / Tea, Fresh Banana",
        "lunch": "Kadai Paneer, Panchmel Mix Dal, Jeera Rice, Tawa Chapati, Cucumber & Onion Salad, Mixed Pickle",
        "tea_snacks": "Bakery Biscuits / Cookies, Hot Ginger Tea",
        "dinner": "South Indian Sambhar, Cabbage / Cauliflower Sabji, Steamed Rice, Hot Chapati, Fresh Salad, Sweet Dish (Sewaiya Kheer)"
    },
    "Thursday": {
        "breakfast": "Onion Mix Stuffed Paratha, Amul Butter, Mint Chutney, Fresh Curd (Dahi), Hot Tea, Fresh Seasonal Fruits",
        "lunch": "Kadhi Pakoda, Aloo-Kala Channa Masala, Steamed Rice, Hot Chapati, Kachumber Salad, Mixed Pickle",
        "tea_snacks": "Crispy Finger Chips (French Fries) / Mix Veg Pakodi, Tomato Ketchup, Hot Coffee",
        "dinner": "Dal Arhar, Baingan Ka Bharta / Pat Gobhi (Cabbage), Steamed Rice, Hot Chapati, Salad, Sweet Dish (Hot Gulab Jamun)"
    },
    "Friday": {
        "breakfast": "Option A: Steamed Idli Sambhar with Coconut Chutney & Grilled Aloo Sandwich | Option B: Kala Chana, Daliya, Sandwich, Coffee/Tea, Apple",
        "lunch": "Pindi Chole Masala, Kaddu (Pumpkin) / Aloo Palak, Steamed Rice, Tawa Chapati, Fresh Salad, Mixed Pickle, Fresh Dahi",
        "tea_snacks": "Cheesy Macaroni Pasta, Tomato Ketchup, Spicy Mumbai Bhel Puri, Hot Tea",
        "dinner": "Dal Masoor, Veg Manchurian / Matar Paneer, Steamed Fried Rice, Chapati, Salad, Sweet Dish (Chilled Fruit Milk Custard)"
    },
    "Saturday": {
        "breakfast": "Palak Paratha / Aloo Paneer Mix Bhurji, Amul Packed Butter, Tangy Chutney, Mixed Pickle, Hot Tea / Banana",
        "lunch": "Dal Malka, Seasonal Mix Veg, Steamed Basmati Rice, Hot Chapati, Green Salad, Pickle, Fried Papad",
        "tea_snacks": "Crispy Punjabi Samosa / Aloo Bonda, Mint Chutney, Tomato Ketchup, Masala Tea",
        "dinner": "Rajma Masala / Aloo Matar, Steamed Rice, Hot Chapati, Fresh Salad, Mixed Pickle, Sweet Dish (Desi Ghee Suji Halwa)"
    },
    "Sunday": {
        "breakfast": "Fluffy Chole Bhature with Pickled Green Chilli & Onion Salad, Mixed Pickle, Special Sunday Chai",
        "lunch": "Special Veg Dum Biryani / Fried Rice, Boondi / Mixed Veg Raita, Mint Chutney, Fried Papad",
        "tea_snacks": "Crunchy Biscuits / Cookies, Special Evening Tea",
        "dinner": "Chana Dal / Urad Dhuli, Aloo Bharta / Sambhar, Steamed Rice, Hot Chapati, Fresh Salad, Sweet Dish (Vanilla Ice Cream / White Sponge Rasgulla)"
    }
}

# ============================================================================
# 2. CAMPUS CANTEEN MENU (BURGERS, MOMOS, COLD DRINKS, COFFEE, TEA, SNACKS)
# ============================================================================
CANTEEN_MENU = {
    "Burgers": [
        {"name": "Crispy Veg Burger", "price": "Rs. 50", "desc": "Crispy vegetable patty, lettuce, mayo & house dressing"},
        {"name": "Cheese Lava Burger", "price": "Rs. 70", "desc": "Loaded with melted mozzarella slice & herb seasoning"},
        {"name": "Paneer Supreme Burger", "price": "Rs. 80", "desc": "Golden fried spiced paneer patty with spicy schezwan sauce"},
        {"name": "Aloo Tikki Street Burger", "price": "Rs. 40", "desc": "Desi spiced potato patty with mint mayo & crunchy onions"}
    ],
    "Momos (Full Plate - 8 Pieces)": [
        {"name": "Veg Steamed Momos (Full Plate)", "price": "Rs. 60", "desc": "8 freshly steamed dumplings with red chilli garlic chutney & mayo"},
        {"name": "Veg Fried Momos (Full Plate)", "price": "Rs. 70", "desc": "8 crispy golden fried dumplings with spicy dip"},
        {"name": "Paneer Steamed Momos (Full Plate)", "price": "Rs. 80", "desc": "8 soft dumplings stuffed with seasoned malai paneer"},
        {"name": "Paneer Fried Momos (Full Plate)", "price": "Rs. 90", "desc": "8 crispy fried paneer dumplings served piping hot"},
        {"name": "Kurkure Crunch Momos (Full Plate)", "price": "Rs. 100", "desc": "8 batter-crusted super crunchy momos with peri-peri sprinkle"}
    ],
    "Cold Drinks & Chilled Beverages": [
        {"name": "Coca-Cola (500 ml Chilled)", "price": "Rs. 40", "desc": "Ice chilled bottle"},
        {"name": "Thums Up (500 ml Chilled)", "price": "Rs. 40", "desc": "Charged strong carbonated cola"},
        {"name": "Sprite (500 ml Chilled)", "price": "Rs. 40", "desc": "Refreshing lemon-lime soda"},
        {"name": "Mountain Dew (500 ml)", "price": "Rs. 40", "desc": "High energy citrus drink"},
        {"name": "Frooti Mango Drink", "price": "Rs. 20", "desc": "Mango pulp refreshment"},
        {"name": "Red Bull Energy Drink", "price": "Rs. 125", "desc": "250 ml can"}
    ],
    "Coffee & Hot Beverages": [
        {"name": "Special Masala Chai", "price": "Rs. 15", "desc": "Freshly brewed with crushed cardamom & ginger"},
        {"name": "Kadak Ginger Tea", "price": "Rs. 15", "desc": "Strong invigorating tea"},
        {"name": "Hot Nescafe Coffee", "price": "Rs. 25", "desc": "Rich milk froth coffee"},
        {"name": "Black Coffee / Green Tea", "price": "Rs. 20", "desc": "Pure energizing black brew / antioxidant green tea"}
    ],
    "Cold Coffee & Shakes": [
        {"name": "Classic Thick Cold Coffee", "price": "Rs. 50", "desc": "Creamy blended cold coffee with chocolate drizzle"},
        {"name": "Cold Coffee with Vanilla Ice Cream", "price": "Rs. 70", "desc": "Thick cold coffee topped with a rich vanilla scoop"},
        {"name": "Chocolate Frappe Cold Coffee", "price": "Rs. 80", "desc": "Blended with Belgian chocolate syrup & choco chips"},
        {"name": "Oreo KitKat Shake", "price": "Rs. 90", "desc": "Creamy shake loaded with crushed Oreo and KitKat"}
    ],
    "Snacks & Quick Bites": [
        {"name": "Classic Salted French Fries", "price": "Rs. 60", "desc": "Crispy golden potato fries with ketchup"},
        {"name": "Peri Peri Masala Fries", "price": "Rs. 75", "desc": "Tossed in fiery African peri peri spice"},
        {"name": "Classic Maggi Noodles", "price": "Rs. 35", "desc": "Piping hot 2-minute masala Maggi"},
        {"name": "Veg Cheese Masala Maggi", "price": "Rs. 55", "desc": "Loaded with chopped veggies & grated cheese"},
        {"name": "Grilled Cheese Sandwich", "price": "Rs. 60", "desc": "Toasted jumbo bread with veggies & cheese"},
        {"name": "Paneer Tikka Grilled Sandwich", "price": "Rs. 75", "desc": "Marinated paneer slices grilled to perfection"}
    ]
}

# ============================================================================
# 3. OFFICIAL CLASS TIMETABLES (1ST, 2ND, 3RD, 4TH YEAR - MON TO SAT COMPLETE)
# ============================================================================
TIMETABLES = {
    # ---------------- 1ST YEAR (B.TECH CSE SEC A - ROOM B-001) ----------------
    "1st_year": {
        "title": "1st Year (B.Tech CSE Section A)",
        "classroom": "Block B - Room B-001",
        "days": {
            "Monday": [
                {"time": "09:05 - 09:55 AM", "subject": "Engineering Mathematics-I (AHT-003)", "faculty": "Dr. S. K. Iyer", "room": "B-001"},
                {"time": "09:55 - 10:45 AM", "subject": "Programming for Problem Solving (CST-001)", "faculty": "Mr. Gaurav Chaturvedi", "room": "B-001"},
                {"time": "11:05 - 01:15 PM", "subject": "Physics Lab (AHP-001) / Electrical Lab (EEP-001)", "faculty": "Dr. Atma Rai / Mr. Ankit Mainwal", "room": "B-101 / C-015"},
                {"time": "01:45 - 02:35 PM", "subject": "Basic Electrical Engineering (EET-001)", "faculty": "Mr. Ankit Mainwal", "room": "B-001"},
                {"time": "02:35 - 03:25 PM", "subject": "Self Employment & Entrepreneurship (AHP-005)", "faculty": "Mr. Abhishek Jain", "room": "B-001"}
            ],
            "Tuesday": [
                {"time": "09:05 - 09:55 AM", "subject": "Engineering Mathematics-I (AHT-003)", "faculty": "Dr. S. K. Iyer", "room": "B-001"},
                {"time": "09:55 - 10:45 AM", "subject": "Programming for Problem Solving (CST-001)", "faculty": "Mr. Gaurav Chaturvedi", "room": "B-001"},
                {"time": "11:05 - 11:55 AM", "subject": "Engineering Physics (AHT-001)", "faculty": "Dr. Atma Rai", "room": "B-001"},
                {"time": "11:55 - 12:45 PM", "subject": "Engineering Graphics Tutorial (MEP-002)", "faculty": "Mr. Narendra Bansal", "room": "B-001"},
                {"time": "01:45 - 03:25 PM", "subject": "Digital Marketing Lab (AHP-003)", "faculty": "Mr. Harsh Dharia", "room": "B-105"}
            ],
            "Wednesday": [
                {"time": "09:05 - 09:55 AM", "subject": "Engineering Mathematics-I (AHT-003)", "faculty": "Dr. S. K. Iyer", "room": "B-001"},
                {"time": "09:55 - 10:45 AM", "subject": "Programming for Problem Solving (CST-001)", "faculty": "Mr. Gaurav Chaturvedi", "room": "B-001"},
                {"time": "11:05 - 11:55 AM", "subject": "Programming for Problem Solving (CST-001)", "faculty": "Mr. Gaurav Chaturvedi", "room": "B-001"},
                {"time": "11:55 - 12:45 PM", "subject": "Basic Electrical Engineering (EET-001)", "faculty": "Mr. Ankit Mainwal", "room": "B-001"},
                {"time": "01:45 - 03:25 PM", "subject": "Engineering Graphics (MEP-002) / C Lab (CSP-001)", "faculty": "Mr. Narendra Bansal / Dr. Neeraj Kumar", "room": "C-310 / A-101"}
            ],
            "Thursday": [
                {"time": "09:05 - 09:55 AM", "subject": "Engineering Mathematics-I (AHT-003)", "faculty": "Dr. S. K. Iyer", "room": "B-001"},
                {"time": "09:55 - 10:45 AM", "subject": "Programming for Problem Solving (CST-001)", "faculty": "Mr. Gaurav Chaturvedi", "room": "B-001"},
                {"time": "11:05 - 11:55 AM", "subject": "Engineering Physics (AHT-001)", "faculty": "Dr. Atma Rai", "room": "B-001"},
                {"time": "11:55 - 12:45 PM", "subject": "Basic Electrical Engineering (EET-001)", "faculty": "Mr. Ankit Mainwal", "room": "B-001"},
                {"time": "01:45 - 03:25 PM", "subject": "Physics Lab (AHP-001) / Electrical Lab (EEP-001)", "faculty": "Dr. Atma Rai / Mr. Ankit Mainwal", "room": "B-101 / C-015"}
            ],
            "Friday": [
                {"time": "09:05 - 09:55 AM", "subject": "Graphics Lab (MEP-002) / C Lab (CSP-001)", "faculty": "Mr. Narendra Bansal / Dr. Neeraj Kumar", "room": "C-310 / A-101"},
                {"time": "11:05 - 11:55 AM", "subject": "Engineering Physics (AHT-001)", "faculty": "Dr. Atma Rai", "room": "B-001"},
                {"time": "11:55 - 12:45 PM", "subject": "Basic Electrical Engineering (EET-001)", "faculty": "Mr. Ankit Mainwal", "room": "B-001"},
                {"time": "01:45 - 02:35 PM", "subject": "Environmental Studies (AHT-004)", "faculty": "Dr. Sandeep Joshi", "room": "B-001"},
                {"time": "02:35 - 03:25 PM", "subject": "Self Employment & Entrepreneurship (AHP-005)", "faculty": "Mr. Abhishek Jain", "room": "B-001"}
            ],
            "Saturday": [
                {"time": "09:05 - 09:55 AM", "subject": "Engineering Mathematics-I Tutorial (AHT-003)", "faculty": "Dr. S. K. Iyer", "room": "B-001"},
                {"time": "09:55 - 10:45 AM", "subject": "Programming Tutorial (CST-001)", "faculty": "Mr. Gaurav Chaturvedi", "room": "B-001"},
                {"time": "11:05 - 11:55 AM", "subject": "Engineering Physics Tutorial (AHT-001)", "faculty": "Dr. Atma Rai", "room": "B-001"},
                {"time": "11:55 - 12:45 PM", "subject": "Electrical Engineering Tutorial (EET-001)", "faculty": "Mr. Ankit Mainwal", "room": "B-001"},
                {"time": "01:45 - 02:35 PM", "subject": "Environmental Studies (AHT-004)", "faculty": "Dr. Sandeep Joshi", "room": "B-001"},
                {"time": "02:35 - 03:25 PM", "subject": "Central Library Reading Session", "faculty": "Library Staff", "room": "Central Library"}
            ]
        }
    },

    # ---------------- 2ND YEAR (B.TECH CSE SEC IIA-A - ROOM C-202) ----------------
    "2nd_year": {
        "title": "2nd Year (B.Tech CSE Section IIA-A)",
        "classroom": "Block C - Room C-202 (2nd Floor)",
        "days": {
            "Monday": [
                {"time": "09:05 - 09:55 AM", "subject": "Object Oriented Programming (CST-004)", "faculty": "Ms. Dimpi Madan", "room": "C-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Universal Human Values (AHT-008)", "faculty": "Dr. Rashmi Gupta", "room": "C-202"},
                {"time": "11:05 - 11:55 AM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-202"},
                {"time": "11:55 - 12:45 PM", "subject": "OOPs Lab (CSP-004) / DSA Lab (CSP-003)", "faculty": "Ms. Dimpi Madan / Dr. Himanshu Gupta", "room": "B-208 / B-206"},
                {"time": "01:45 - 04:15 PM", "subject": "GeeksforGeeks (GFG) Elite Coding Track", "faculty": "Coding Mentors", "room": "C-202 / C-204"}
            ],
            "Tuesday": [
                {"time": "09:05 - 09:55 AM", "subject": "Discrete Structure (CST-002)", "faculty": "Dr. Akshay Saini", "room": "C-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Object Oriented Programming (CST-004)", "faculty": "Ms. Dimpi Madan", "room": "C-202"},
                {"time": "11:05 - 11:55 AM", "subject": "Data Structures & Algorithms (CST-003)", "faculty": "Dr. Himanshu Gupta", "room": "C-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Object Oriented Programming (CST-004)", "faculty": "Ms. Dimpi Madan", "room": "C-202"},
                {"time": "01:45 - 04:15 PM", "subject": "GeeksforGeeks (GFG) Elite Problem Solving", "faculty": "Coding Mentors", "room": "C-202 / C-204"}
            ],
            "Wednesday": [
                {"time": "09:05 - 09:55 AM", "subject": "Universal Human Values (AHT-008)", "faculty": "Dr. Rashmi Gupta", "room": "C-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Data Structures & Algorithms (CST-003)", "faculty": "Dr. Himanshu Gupta", "room": "C-202"},
                {"time": "11:05 - 11:55 AM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Digital Electronics (ECT-033)", "faculty": "Dr. Ranjan Mishra", "room": "C-202"},
                {"time": "01:45 - 04:15 PM", "subject": "GeeksforGeeks (GFG) Competitive Coding", "faculty": "Coding Mentors", "room": "C-202 / C-204"}
            ],
            "Thursday": [
                {"time": "09:05 - 09:55 AM", "subject": "Python Programming (CST-005)", "faculty": "Dr. Deepak Arya", "room": "C-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Digital Electronics (ECT-033)", "faculty": "Dr. Ranjan Mishra", "room": "C-202"},
                {"time": "11:05 - 11:55 AM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Discrete Structure (CST-002)", "faculty": "Dr. Akshay Saini", "room": "C-202"},
                {"time": "01:45 - 04:15 PM", "subject": "GeeksforGeeks (GFG) Elite Coding Practice", "faculty": "Coding Mentors", "room": "C-202 / C-204"}
            ],
            "Friday": [
                {"time": "09:05 - 09:55 AM", "subject": "OOPs Lab (CSP-004) / Python Lab (CSP-005)", "faculty": "Ms. Dimpi Madan / Dr. Deepak Arya", "room": "B-106 / B-207"},
                {"time": "09:55 - 10:45 AM", "subject": "Data Structures & Algorithms (CST-003)", "faculty": "Dr. Himanshu Gupta", "room": "C-202"},
                {"time": "11:05 - 11:55 AM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Data Structures & Algorithms (CST-003)", "faculty": "Dr. Himanshu Gupta", "room": "C-202"},
                {"time": "01:45 - 04:15 PM", "subject": "GeeksforGeeks (GFG) Elite Coding Practice", "faculty": "Coding Mentors", "room": "C-202 / C-204"}
            ],
            "Saturday": [
                {"time": "09:05 - 09:55 AM", "subject": "Digital Electronics (ECT-033)", "faculty": "Dr. Ranjan Mishra", "room": "C-202"},
                {"time": "09:55 - 10:45 AM", "subject": "DSA Lab (CSP-003) / Python Lab (CSP-005)", "faculty": "Dr. Himanshu Gupta / Dr. Deepak Arya", "room": "B-208 / B-207"},
                {"time": "11:05 - 11:55 AM", "subject": "Discrete Structure (CST-002)", "faculty": "Dr. Akshay Saini", "room": "C-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Object Oriented Programming (CST-004)", "faculty": "Ms. Dimpi Madan", "room": "C-202"},
                {"time": "01:45 - 04:15 PM", "subject": "GeeksforGeeks (GFG) Weekly Contest & Hackathon", "faculty": "Coding Mentors", "room": "C-202 / C-204"}
            ]
        }
    },

    # ---------------- 3RD YEAR (B.TECH CSE SEC IIIA-A - ROOM C-212) ----------------
    "3rd_year": {
        "title": "3rd Year (B.Tech CSE Section IIIA-A)",
        "classroom": "Block C - Room C-212 (2nd Floor)",
        "days": {
            "Monday": [
                {"time": "09:05 - 10:45 AM", "subject": "GeeksforGeeks (GFG) Regular/Elite Track", "faculty": "GFG Mentors", "room": "C-212 / C-214"},
                {"time": "11:05 - 11:55 AM", "subject": "Compiler Design (CST-012)", "faculty": "Ms. Bhanupriya", "room": "C-212"},
                {"time": "11:55 - 12:45 PM", "subject": "Software Engineering (CST-015)", "faculty": "Ms. Chandani", "room": "C-212"},
                {"time": "01:45 - 03:25 PM", "subject": "DBMS Lab (CSP-011) / Compiler Lab (CSP-012)", "faculty": "Ms. Priti Saini / Ms. Bhanupriya", "room": "C-012 / B-105"},
                {"time": "03:25 - 04:15 PM", "subject": "Design & Analysis of Algorithms (CST-010)", "faculty": "Mr. Vipin Jaiswal", "room": "C-212"},
                {"time": "04:15 - 05:00 PM", "subject": "Database Management Systems (CST-011)", "faculty": "Ms. Priti Saini", "room": "C-212"}
            ],
            "Tuesday": [
                {"time": "09:05 - 10:45 AM", "subject": "GeeksforGeeks (GFG) Regular/Elite Track", "faculty": "GFG Mentors", "room": "C-212 / C-214"},
                {"time": "11:05 - 11:55 AM", "subject": "Compiler Design (CST-012)", "faculty": "Ms. Bhanupriya", "room": "C-212"},
                {"time": "11:55 - 12:45 PM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-212"},
                {"time": "01:45 - 02:35 PM", "subject": "Distributed Systems (CST-019)", "faculty": "Dr. Abhay Bhatia", "room": "C-212"},
                {"time": "02:35 - 03:25 PM", "subject": "Design & Analysis of Algorithms (CST-010)", "faculty": "Mr. Vipin Jaiswal", "room": "C-212"},
                {"time": "03:25 - 05:00 PM", "subject": "DBMS Lab (CSP-011) / DAA Lab (CSP-010)", "faculty": "Ms. Priti Saini / Mr. Vipin Jaiswal", "room": "C-012 / B-106"}
            ],
            "Wednesday": [
                {"time": "09:05 - 10:45 AM", "subject": "GeeksforGeeks (GFG) Regular/Elite Track", "faculty": "GFG Mentors", "room": "C-212 / C-214"},
                {"time": "11:05 - 11:55 AM", "subject": "Compiler Design (CST-012)", "faculty": "Ms. Bhanupriya", "room": "C-212"},
                {"time": "11:55 - 12:45 PM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-212"},
                {"time": "01:45 - 02:35 PM", "subject": "Database Management Systems (CST-011)", "faculty": "Ms. Priti Saini", "room": "C-212"},
                {"time": "02:35 - 03:25 PM", "subject": "Design & Analysis of Algorithms (CST-010)", "faculty": "Mr. Vipin Jaiswal", "room": "C-212"},
                {"time": "03:25 - 04:15 PM", "subject": "Distributed Systems (CST-019)", "faculty": "Dr. Abhay Bhatia", "room": "C-212"},
                {"time": "04:15 - 05:00 PM", "subject": "Software Engineering (CST-015)", "faculty": "Ms. Chandani", "room": "C-212"}
            ],
            "Thursday": [
                {"time": "09:05 - 10:45 AM", "subject": "GeeksforGeeks (GFG) Problem Solving Track", "faculty": "GFG Mentors", "room": "C-212 / C-214"},
                {"time": "11:05 - 11:55 AM", "subject": "Design & Analysis of Algorithms (CST-010)", "faculty": "Mr. Vipin Jaiswal", "room": "C-212"},
                {"time": "11:55 - 12:45 PM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-212"},
                {"time": "01:45 - 02:35 PM", "subject": "Compiler Design (CST-012)", "faculty": "Ms. Bhanupriya", "room": "C-212"},
                {"time": "02:35 - 03:25 PM", "subject": "Database Management Systems (CST-011)", "faculty": "Ms. Priti Saini", "room": "C-212"},
                {"time": "03:25 - 05:00 PM", "subject": "DAA Lab (CSP-010) / Compiler Lab (CSP-012)", "faculty": "Mr. Vipin Jaiswal / Ms. Bhanupriya", "room": "B-106 / B-208"}
            ],
            "Friday": [
                {"time": "09:05 - 10:45 AM", "subject": "GeeksforGeeks (GFG) Coding Contest", "faculty": "GFG Mentors", "room": "C-212 / C-214"},
                {"time": "11:05 - 11:55 AM", "subject": "Constitution of India (AHT-009)", "faculty": "Mr. Rao Ragib Khan", "room": "C-212"},
                {"time": "11:55 - 12:45 PM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-212"},
                {"time": "01:45 - 02:35 PM", "subject": "Distributed Systems (CST-019)", "faculty": "Dr. Abhay Bhatia", "room": "C-212"},
                {"time": "02:35 - 03:25 PM", "subject": "Software Engineering (CST-015)", "faculty": "Ms. Chandani", "room": "C-212"},
                {"time": "03:25 - 04:15 PM", "subject": "Database Management Systems (CST-011)", "faculty": "Ms. Priti Saini", "room": "C-212"}
            ],
            "Saturday": [
                {"time": "09:05 - 10:45 AM", "subject": "GeeksforGeeks (GFG) Weekly Sprint", "faculty": "GFG Mentors", "room": "C-212 / C-214"},
                {"time": "11:05 - 11:55 AM", "subject": "Database Management Systems (CST-011)", "faculty": "Ms. Priti Saini", "room": "C-212"},
                {"time": "11:55 - 12:45 PM", "subject": "Design & Analysis of Algorithms (CST-010)", "faculty": "Mr. Vipin Jaiswal", "room": "C-212"},
                {"time": "01:45 - 02:35 PM", "subject": "Distributed Systems (CST-019)", "faculty": "Dr. Abhay Bhatia", "room": "C-212"},
                {"time": "02:35 - 03:25 PM", "subject": "Software Engineering (CST-015)", "faculty": "Ms. Chandani", "room": "C-212"},
                {"time": "03:25 - 04:15 PM", "subject": "Compiler Design (CST-012)", "faculty": "Ms. Bhanupriya", "room": "C-212"}
            ]
        }
    },

    # ---------------- 4TH YEAR (B.TECH CSE FINAL YEAR - ROOM D-202) ----------------
    "4th_year": {
        "title": "4th Year (B.Tech CSE Final Year Specialization)",
        "classroom": "Block D - Room D-202 (2nd Floor)",
        "days": {
            "Monday": [
                {"time": "09:05 - 09:55 AM", "subject": "Cloud Computing (CST-037)", "faculty": "Ms. Bhanupriya", "room": "D-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Machine Learning (CST-030)", "faculty": "Dr. Gaurav Kumar", "room": "D-202"},
                {"time": "11:05 - 11:55 AM", "subject": "Advanced Mobile Technology (EEC-066)", "faculty": "Ms. Priti Saini", "room": "D-202"},
                {"time": "01:45 - 02:35 PM", "subject": "Disaster Management (AHT-017)", "faculty": "Dr. Anil Chauhan", "room": "D-202"},
                {"time": "02:35 - 04:15 PM", "subject": "Major Capstone Project Seminar (CSP-018)", "faculty": "Mr. Avnish Chauhan", "room": "D-202 / R&D Lab"}
            ],
            "Tuesday": [
                {"time": "09:05 - 09:55 AM", "subject": "Disaster Management (AHT-017)", "faculty": "Dr. Anil Chauhan", "room": "D-202"},
                {"time": "11:05 - 11:55 AM", "subject": "Advanced Mobile Technology (EEC-066)", "faculty": "Ms. Priti Saini", "room": "D-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Cloud Computing (CST-037)", "faculty": "Ms. Bhanupriya", "room": "D-202"},
                {"time": "01:45 - 02:35 PM", "subject": "Disaster Management (AHT-017)", "faculty": "Mr. Deepak Kumar", "room": "D-202"},
                {"time": "02:35 - 05:00 PM", "subject": "Industry Placement Mock Interviews & Drives", "faculty": "T&P Cell Mentors", "room": "Placement Hall"}
            ],
            "Wednesday": [
                {"time": "09:05 - 09:55 AM", "subject": "Disaster Management (AHT-017)", "faculty": "Dr. Anil Chauhan", "room": "D-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Advanced Mobile Technology (EEC-066)", "faculty": "Ms. Priti Saini", "room": "D-202"},
                {"time": "11:05 - 11:55 AM", "subject": "Innovations & Problem Solving (AHT-018)", "faculty": "Ms. Taniya Dhiman", "room": "D-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Machine Learning (CST-030)", "faculty": "Dr. Gaurav Kumar", "room": "D-202"},
                {"time": "01:45 - 02:35 PM", "subject": "Rural Development & Administration (AHT-015)", "faculty": "Mr. Deepak Kumar", "room": "D-202"},
                {"time": "02:35 - 04:15 PM", "subject": "Major Design Project Prototyping (CSP-019)", "faculty": "Ms. Bhanupriya", "room": "Project Lab"}
            ],
            "Thursday": [
                {"time": "09:05 - 09:55 AM", "subject": "Cloud Computing (CST-037)", "faculty": "Ms. Bhanupriya", "room": "D-202"},
                {"time": "11:05 - 11:55 AM", "subject": "Innovations & Problem Solving (AHT-018)", "faculty": "Ms. Taniya Dhiman", "room": "D-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Disaster Management (AHT-017)", "faculty": "Dr. Anil Chauhan", "room": "D-202"},
                {"time": "01:45 - 03:25 PM", "subject": "Machine Learning Lab & GPU Experiments", "faculty": "Dr. Gaurav Kumar", "room": "AI Lab"},
                {"time": "03:25 - 05:00 PM", "subject": "Startup Pitch & Incubation Reviews", "faculty": "Dean Incubation", "room": "Conference Room"}
            ],
            "Friday": [
                {"time": "09:05 - 09:55 AM", "subject": "Machine Learning (CST-030)", "faculty": "Dr. Gaurav Kumar", "room": "D-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Cloud Computing Architecture (CST-037)", "faculty": "Ms. Bhanupriya", "room": "D-202"},
                {"time": "11:05 - 12:45 PM", "subject": "Design Project Lab & Sprint Demo (CSP-019)", "faculty": "Ms. Bhanupriya", "room": "Project Lab"},
                {"time": "01:45 - 04:15 PM", "subject": "Open Source Contributions & Research Paper Writing", "faculty": "Research Committee", "room": "D-202"}
            ],
            "Saturday": [
                {"time": "09:05 - 11:00 AM", "subject": "Capstone Major Project Presentation & Review", "faculty": "Department Evaluation Panel", "room": "D-202 / Seminar Hall"},
                {"time": "11:15 - 01:15 PM", "subject": "Patent Filing, Ethics & Research Documentation", "faculty": "Dr. Lokesh Kumar (HOD CSE)", "room": "D-202"},
                {"time": "02:00 - 04:00 PM", "subject": "Alumni Mentorship & Placement Preparations", "faculty": "Alumni Relations", "room": "Auditorium"}
            ]
        }
    }
}

# ============================================================================
# 4. CAMPUS BUILDINGS & CLASSROOMS DIRECTORY (RIT CAMPUS)
# ============================================================================
BUILDINGS = {
    "bldg_block_b": {
        "id": "bldg_block_b",
        "name": "Academic Block B",
        "code": "BLOCK-B",
        "total_floors": 4,
        "description": "Houses First Year B.Tech CSE Classrooms (B-001, B-002, B-003), Physics Labs, Computing Labs, and Graphics Halls.",
        "icon_url": "https://images.unsplash.com/photo-1562774053-701939374585?w=600",
        "floors": {
            "Ground Floor": [
                {"room": "B-001", "name": "1st Year B.Tech CSE Section A", "capacity": 75, "type": "Classroom"},
                {"room": "B-002", "name": "1st Year B.Tech CSE Section B", "capacity": 75, "type": "Classroom"},
                {"room": "B-003", "name": "1st Year B.Tech CSE Section C", "capacity": 75, "type": "Classroom"}
            ],
            "1st Floor": [
                {"room": "B-101", "name": "Engineering Physics Lab", "capacity": 60, "type": "Physics Lab"},
                {"room": "B-102", "name": "Engineering Chemistry & Physics Lab", "capacity": 60, "type": "Science Lab"},
                {"room": "B-105", "name": "Digital Marketing & Computing Lab", "capacity": 50, "type": "Computing Lab"},
                {"room": "B-106", "name": "Programming & OOPs Lab (CSP-004)", "capacity": 60, "type": "Software Lab"}
            ],
            "2nd Floor": [
                {"room": "B-206", "name": "Data Structures & Algorithms Lab (CSP-003)", "capacity": 60, "type": "Computing Lab"},
                {"room": "B-207", "name": "Python Programming Lab (CSP-005)", "capacity": 60, "type": "Computing Lab"},
                {"room": "B-208", "name": "Advanced Computing & OOPs Lab", "capacity": 60, "type": "Computing Lab"}
            ]
        }
    },
    "bldg_block_c": {
        "id": "bldg_block_c",
        "name": "Academic Block C (Core CSE & IT)",
        "code": "BLOCK-C",
        "total_floors": 4,
        "description": "Heart of CSE Department: 2nd Year (C-202), 3rd Year (C-212), AI-ML (C-306), HOD Chamber & Apple Mac Lab.",
        "icon_url": "https://images.unsplash.com/photo-1541829070764-84a7d30dd3f3?w=600",
        "floors": {
            "Ground Floor": [
                {"room": "C-012", "name": "Database Management Systems (DBMS) Lab", "capacity": 65, "type": "Software Lab"},
                {"room": "C-015", "name": "Basic Electrical Engineering Lab", "capacity": 55, "type": "Hardware Lab"}
            ],
            "2nd Floor": [
                {"room": "C-201", "name": "HOD CSE Chamber (Dr. Lokesh Kumar)", "capacity": 15, "type": "Faculty"},
                {"room": "C-202", "name": "2nd Year B.Tech CSE Section IIA-A", "capacity": 80, "type": "Classroom"},
                {"room": "C-204", "name": "GeeksforGeeks Coding Arena & Contest Room", "capacity": 80, "type": "Coding Arena"},
                {"room": "C-205", "name": "Dr. Himanshu Gupta (DSA) Cabin", "capacity": 6, "type": "Faculty"},
                {"room": "C-209", "name": "Dr. Deepak Arya (Python) Cabin", "capacity": 6, "type": "Faculty"},
                {"room": "C-212", "name": "3rd Year B.Tech CSE Section IIIA-A", "capacity": 80, "type": "Classroom"},
                {"room": "C-214", "name": "IBM Cloud Innovation Lab", "capacity": 70, "type": "Software Lab"}
            ],
            "3rd Floor": [
                {"room": "C-306", "name": "B.Tech CSE AI & ML Specialization", "capacity": 75, "type": "Classroom"},
                {"room": "C-310", "name": "AutoCAD & Engineering Graphics Computing Hall", "capacity": 70, "type": "Graphics Lab"}
            ]
        }
    },
    "bldg_block_d": {
        "id": "bldg_block_d",
        "name": "Academic Block D (Final Year & Placement)",
        "code": "BLOCK-D",
        "total_floors": 3,
        "description": "Houses 4th Year Classrooms (D-202), Capstone Project Labs, Training & Placement Cell, and Conference Chambers.",
        "icon_url": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=600",
        "floors": {
            "Ground Floor": [
                {"room": "D-001", "name": "Student Training & Placement Cell (T&P)", "capacity": 40, "type": "Admin"},
                {"room": "D-002", "name": "Corporate Interview Rooms", "capacity": 30, "type": "Interview"}
            ],
            "1st Floor": [
                {"room": "D-101", "name": "Dean Academics & Administrative Chambers", "capacity": 20, "type": "Admin"}
            ],
            "2nd Floor": [
                {"room": "D-202", "name": "4th Year Final Year B.Tech CSE Classroom", "capacity": 80, "type": "Classroom"},
                {"room": "D-204", "name": "Capstone Design & Major Project Lab", "capacity": 50, "type": "Research Lab"}
            ]
        }
    },
    "bldg_amenities": {
        "id": "bldg_amenities",
        "name": "Hostel Mess & Central Canteen Complex",
        "code": "AMENITIES",
        "total_floors": 2,
        "description": "Boys Hostel Mess dining hall (Capacity: 650 students), Central Canteen, and Student Activity Center.",
        "icon_url": "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=600",
        "floors": {
            "Ground Floor": [
                {"room": "Boys-Mess", "name": "RIT Boys Hostel Central Dining Mess", "capacity": 650, "type": "Dining"},
                {"room": "Mess-Office", "name": "Food Manager & Chief Warden Desk", "capacity": 10, "type": "Admin"}
            ],
            "1st Floor": [
                {"room": "Canteen", "name": "Campus Cafe & Fast Food Canteen", "capacity": 150, "type": "Canteen"},
                {"room": "Juice-Corner", "name": "Fresh Juice & Cold Coffee Counter", "capacity": 40, "type": "Beverage"}
            ]
        }
    }
}

# ============================================================================
# 5. FACULTY DIRECTORY & CABINS (RIT ROORKEE)
# ============================================================================
FACULTY_MEMBERS = [
    {
        "id": "fac_dr_lokesh",
        "name": "Dr. Lokesh Kumar",
        "designation": "Head of Department (HOD) - CSE",
        "department": "Computer Science & Engineering",
        "subjects": ["Compiler Design (CST-012)", "Advanced Computing Systems"],
        "cabin": "Block C, 2nd Floor, HOD Chamber C-201",
        "email": "lokesh.kumar@ritroorkee.com",
        "office_hours": "Monday & Wednesday: 2:00 PM - 4:00 PM",
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200"
    },
    {
        "id": "fac_dr_atma",
        "name": "Dr. Atma Rai",
        "designation": "Professor & Time Table Coordinator",
        "department": "Applied Science & Humanities",
        "subjects": ["Engineering Physics (AHT-001)", "Engineering Physics Lab (AHP-001)"],
        "cabin": "Block B, 1st Floor, Cabin B-104",
        "email": "atma.rai@ritroorkee.com",
        "office_hours": "Monday to Friday: 12:00 PM - 1:00 PM",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200"
    },
    {
        "id": "fac_himanshu_gupta",
        "name": "Dr. Himanshu Gupta",
        "designation": "Associate Professor",
        "department": "Computer Science & Engineering",
        "subjects": ["Data Structures & Algorithms (CST-003)", "DSA Lab (CSP-003)"],
        "cabin": "Block C, 2nd Floor, Cabin C-205",
        "email": "himanshu.gupta@ritroorkee.com",
        "office_hours": "Tuesday & Thursday: 11:00 AM - 1:00 PM",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200"
    },
    {
        "id": "fac_deepak_arya",
        "name": "Dr. Deepak Arya",
        "designation": "Assistant Professor",
        "department": "Computer Science & Engineering",
        "subjects": ["Python Programming (CST-005)", "Python Programming Lab (CSP-005)"],
        "cabin": "Block C, 2nd Floor, Cabin C-209",
        "email": "deepak.arya@ritroorkee.com",
        "office_hours": "Wednesday & Friday: 2:00 PM - 4:00 PM",
        "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=200"
    },
    {
        "id": "fac_dimpi_madan",
        "name": "Ms. Dimpi Madan",
        "designation": "Assistant Professor",
        "department": "Computer Science & Engineering",
        "subjects": ["Object Oriented Programming (CST-004)", "OOPs Java Lab (CSP-004)"],
        "cabin": "Block C, 2nd Floor, Faculty Cabin C-208",
        "email": "dimpi.madan@ritroorkee.com",
        "office_hours": "Monday & Thursday: 1:00 PM - 3:00 PM",
        "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200"
    },
    {
        "id": "fac_bhanupriya",
        "name": "Ms. Bhanupriya",
        "designation": "Assistant Professor",
        "department": "Computer Science & Engineering",
        "subjects": ["Compiler Design (CST-012)", "Cloud Computing (CST-037)", "Project Lab (CSP-019)"],
        "cabin": "Block C, 2nd Floor, Faculty Cabin C-207",
        "email": "bhanupriya@ritroorkee.com",
        "office_hours": "Tuesday & Friday: 2:00 PM - 4:00 PM",
        "avatar": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=200"
    },
    {
        "id": "fac_priti_saini",
        "name": "Ms. Priti Saini",
        "designation": "Assistant Professor",
        "department": "Computer Science & Engineering",
        "subjects": ["Database Management Systems (CST-011)", "Mobile Technology (EEC-066)", "DBMS Lab (CSP-011)"],
        "cabin": "Block C, 2nd Floor, Faculty Cabin C-210",
        "email": "priti.saini@ritroorkee.com",
        "office_hours": "Monday & Wednesday: 11:00 AM - 1:00 PM",
        "avatar": "https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?w=200"
    }
]

# ============================================================================
# 6. ASI:ONE INTERACTIVE CARD GENERATORS
# ============================================================================
def card_msg(narration: str, kind: str, payload: dict) -> ChatMessage:
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
                    "requires_card_interaction": "true",
                    "card_kind": kind,
                    "card_payload": json.dumps(payload),
                    "preferred_drawer_width_px": "540"
                }
            )
        ]
    )

def main_menu_carousel():
    return {
        "title": "CampusMitra AI: Smart Campus Concierge",
        "subtitle": "Timetables, Hostel Mess Food, Canteen, Classrooms & Faculty",
        "items": [
            {
                "id": "menu_timetables",
                "image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=600",
                "title": "Class Timetables (1st - 4th Year)",
                "subtitle": "Mon-Sat routines, venues (B-001, C-202, C-212, D-202)",
                "badges": [{"label": "All 4 Years", "variant": "success"}],
                "secondary_text": "Live weekly schedules and lab allocations",
                "primary_cta": {"label": "Browse Timetables", "selection": {"action": "menu_timetables"}}
            },
            {
                "id": "menu_mess",
                "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600",
                "title": "Boys Hostel Mess Food",
                "subtitle": "Breakfast, Lunch, Tea/Snacks & Dinner",
                "badges": [{"label": "All 7 Days", "variant": "warning"}],
                "secondary_text": "Aloo Paratha, Shahi Paneer, Chole Bhature, Kheer & Ice Cream",
                "primary_cta": {"label": "View Mess Menu", "selection": {"action": "menu_mess"}}
            },
            {
                "id": "menu_canteen",
                "image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600",
                "title": "Campus Canteen Menu",
                "subtitle": "Burgers, Full Plate Momos, Cold Drinks, Cold Coffee",
                "badges": [{"label": "Fast Food", "variant": "info"}],
                "secondary_text": "Burgers, Momos, Cold Coffee, Masala Tea & Fries",
                "primary_cta": {"label": "View Canteen Menu", "selection": {"action": "menu_canteen"}}
            },
            {
                "id": "menu_buildings",
                "image": "https://images.unsplash.com/photo-1562774053-701939374585?w=600",
                "title": "Campus Buildings & Rooms",
                "subtitle": "Block B, Block C, Block D & Amenities",
                "badges": [{"label": "Floor Maps", "variant": "success"}],
                "secondary_text": "Navigate to B-001, C-202, C-212, D-202, labs and cabins",
                "primary_cta": {"label": "Explore Buildings", "selection": {"action": "menu_buildings"}}
            },
            {
                "id": "menu_faculty",
                "image": "https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=600",
                "title": "Faculty & Cabin Directory",
                "subtitle": "HOD CSE, Professors, Subjects & Visiting Hours",
                "badges": [{"label": "Faculty Directory", "variant": "info"}],
                "secondary_text": "Dr. Lokesh Kumar, Dr. Atma Rai, Dr. Himanshu Gupta",
                "primary_cta": {"label": "View Faculty", "selection": {"action": "menu_faculty"}}
            }
        ]
    }

def mess_days_carousel():
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
        "subtitle": "Breakfast (7:30 AM), Lunch (12:45 PM), Tea (5:15 PM), Dinner (8:00 PM)",
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

def mess_detail_card(day="Monday"):
    day_norm = day.capitalize()
    meals = MESS_MENU.get(day_norm, MESS_MENU["Monday"])
    rows = [
        {"label": f"🍳 Breakfast ({MESS_TIMINGS['breakfast']})", "value": meals["breakfast"]},
        {"label": f"🍛 Lunch ({MESS_TIMINGS['lunch']})", "value": meals["lunch"]},
        {"label": f"☕ Tea & Snacks ({MESS_TIMINGS['tea_snacks']})", "value": meals["tea_snacks"]},
        {"label": f"🍲 Dinner ({MESS_TIMINGS['dinner']})", "value": meals["dinner"]}
    ]
    next_days = {
        "Monday": "Tuesday", "Tuesday": "Wednesday", "Wednesday": "Thursday",
        "Thursday": "Friday", "Friday": "Saturday", "Saturday": "Sunday", "Sunday": "Monday"
    }
    next_day = next_days.get(day_norm, "Monday")
    return {
        "title": f"RIT Boys Hostel Mess: {day_norm}",
        "hero_image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600",
        "summary_rows": rows,
        "approve_cta": {"label": f"View {next_day}'s Food", "primary": True, "selection": {"action": "view_mess", "day": next_day}},
        "reject_cta": {"label": "All Days Menu", "selection": {"action": "menu_mess"}}
    }

def canteen_carousel():
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

def canteen_detail_card(cat="Burgers"):
    items = CANTEEN_MENU.get(cat, CANTEEN_MENU["Burgers"])
    rows = [{"label": f"{it['name']} ({it['price']})", "value": it["desc"]} for it in items]
    return {
        "title": f"Canteen: {cat}",
        "hero_image": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600",
        "summary_rows": rows,
        "approve_cta": {"label": "Explore Other Categories", "primary": True, "selection": {"action": "menu_canteen"}},
        "reject_cta": {"label": "Main Menu", "selection": {"action": "main_menu"}}
    }

def timetables_year_carousel():
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

def timetable_detail_card(year_key="1st_year", day="Monday"):
    day_norm = day.capitalize()
    tt = TIMETABLES.get(year_key, TIMETABLES["1st_year"])
    schedule = tt["days"].get(day_norm, tt["days"].get("Monday", []))
    rows = [
        {"label": "Classroom", "value": tt["classroom"]},
        {"label": "Day", "value": day_norm}
    ]
    for slot in schedule:
        rows.append({"label": slot["time"], "value": f"{slot['subject']} | Room: {slot['room']} ({slot['faculty']})"})

    next_days = {"Monday": "Tuesday", "Tuesday": "Wednesday", "Wednesday": "Thursday", "Thursday": "Friday", "Friday": "Saturday", "Saturday": "Monday"}
    next_day = next_days.get(day_norm, "Monday")

    return {
        "title": f"Schedule: {tt['title']} ({day_norm})",
        "hero_image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=600",
        "summary_rows": rows,
        "approve_cta": {"label": f"View {next_day}'s Schedule", "primary": True, "selection": {"action": "view_timetable", "year": year_key, "day": next_day}},
        "reject_cta": {"label": "Change Year", "selection": {"action": "menu_timetables"}}
    }

def buildings_carousel():
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
                "primary_cta": {"label": "View Floor Map & Rooms", "selection": {"action": "view_building", "bldg_id": b["id"]}}
            }
            for b in BUILDINGS.values()
        ]
    }

def building_detail_card(bldg_id="bldg_block_b"):
    b = BUILDINGS.get(bldg_id, BUILDINGS["bldg_block_b"])
    rows = [
        {"label": "Building Code", "value": b["code"]},
        {"label": "Total Floors", "value": f"{b['total_floors']} Floors"},
        {"label": "Overview", "value": b["description"]}
    ]
    for floor, rooms in b["floors"].items():
        room_strs = [f"{r['room']} ({r['name']})" for r in rooms]
        rows.append({"label": floor, "value": " • ".join(room_strs)})

    return {
        "title": b["name"],
        "hero_image": b["icon_url"],
        "summary_rows": rows,
        "approve_cta": {"label": "Explore Other Buildings", "primary": True, "selection": {"action": "menu_buildings"}},
        "reject_cta": {"label": "Main Menu", "selection": {"action": "main_menu"}}
    }

def faculty_carousel():
    return {
        "title": "Faculty Directory & Cabins (RIT)",
        "subtitle": "Explore professors, department designations, subjects, and visiting hours",
        "items": [
            {
                "id": f["id"],
                "image": f["avatar"],
                "title": f["name"],
                "subtitle": f"{f['designation']} ({f['department']})",
                "badges": [{"label": f["cabin"].split(',')[0], "variant": "info"}],
                "secondary_text": f"Cabin: {f['cabin']} | Hours: {f['office_hours']}",
                "primary_cta": {"label": "View Cabin & Subjects", "selection": {"action": "view_faculty", "faculty_id": f["id"]}}
            }
            for f in FACULTY_MEMBERS
        ]
    }

def faculty_detail_card(faculty_id="fac_dr_lokesh"):
    faculty = next((f for f in FACULTY_MEMBERS if f["id"] == faculty_id), FACULTY_MEMBERS[0])
    rows = [
        {"label": "Professor Name", "value": faculty["name"]},
        {"label": "Designation", "value": faculty["designation"]},
        {"label": "Department", "value": faculty["department"]},
        {"label": "Teaching Subjects", "value": ", ".join(faculty["subjects"])},
        {"label": "Office / Cabin Location", "value": faculty["cabin"]},
        {"label": "Official Email", "value": faculty["email"]},
        {"label": "Visiting Hours", "value": faculty["office_hours"]}
    ]
    return {
        "title": f"Faculty: {faculty['name']}",
        "hero_image": faculty["avatar"],
        "summary_rows": rows,
        "approve_cta": {"label": "Explore All Faculty", "primary": True, "selection": {"action": "menu_faculty"}},
        "reject_cta": {"label": "Main Menu", "selection": {"action": "main_menu"}}
    }


# ============================================================================
# 7. AGENT INITIALIZATION & INTERACTIVE PROTOCOL
# ============================================================================
agent = Agent(name="campus_mitra_cloud", seed="campus-mitra-asi-cloud-2026-seed")
chat_proto = Protocol(spec=chat_protocol_spec)

@chat_proto.on_message(ChatMessage)
async def on_message(ctx: Context, sender: str, msg: ChatMessage):
    # Acknowledge immediately
    await ctx.send(sender, ChatAcknowledgement(timestamp=datetime.now(timezone.utc), acknowledged_msg_id=msg.msg_id))

    text = next((c.text for c in msg.content if isinstance(c, TextContent)), "").strip()
    lower = text.lower()

    action_data = {}
    if text.startswith("{") and text.endswith("}"):
        try:
            action_data = json.loads(text)
        except Exception:
            pass

    action = action_data.get("action", "")

    # 1. GREETING OR MAIN MENU
    if not text or lower in {"hi", "hello", "start", "menu", "help"} or action == "main_menu":
        await ctx.send(sender, card_msg(
            "👋 **Namaste! Welcome to CampusMitra AI (Roorkee Institute of Technology).**\n\nI can help you with class timetables, hostel mess food, campus canteen orders, classroom floor navigation, and faculty cabins. Select a service below:",
            "carousel",
            main_menu_carousel()
        ))
        return

    # 2. MESS FOOD HANDLER
    if action == "menu_mess":
        await ctx.send(sender, card_msg(
            "🍲 **RIT Boys Hostel Mess: Select a day to view Breakfast, Lunch, Snacks & Dinner**:",
            "carousel",
            mess_days_carousel()
        ))
        return

    if action == "view_mess" or any(w in lower for w in ["mess", "breakfast", "lunch", "dinner", "kheer", "paratha", "chole bhature", "jalebi"]):
        day = action_data.get("day", "Monday")
        for d in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            if d in lower:
                day = d.capitalize()
                break
        await ctx.send(sender, card_msg(
            f"🍲 **RIT Boys Hostel Mess Menu ({day})**:",
            "detail",
            mess_detail_card(day)
        ))
        return

    # 3. CANTEEN MENU HANDLER
    if action == "menu_canteen":
        await ctx.send(sender, card_msg(
            "🍔 **Campus Canteen Menu: Select a category to explore items and prices**:",
            "carousel",
            canteen_carousel()
        ))
        return

    if action == "view_canteen_category" or any(w in lower for w in ["canteen", "burger", "momo", "cold drink", "coke", "thums up", "sprite", "dew", "coffee", "tea", "chai", "cold coffee", "shake", "fries", "maggi", "sandwich"]):
        cat = action_data.get("category", "Burgers")
        if "momo" in lower:
            cat = "Momos (Full Plate - 8 Pieces)"
        elif any(w in lower for w in ["cold drink", "coke", "thums up", "sprite", "dew", "frooti", "red bull"]):
            cat = "Cold Drinks & Chilled Beverages"
        elif any(w in lower for w in ["cold coffee", "frappe", "shake", "oreo"]):
            cat = "Cold Coffee & Shakes"
        elif any(w in lower for w in ["tea", "chai", "hot coffee", "nescafe"]):
            cat = "Coffee & Hot Beverages"
        elif any(w in lower for w in ["fries", "maggi", "sandwich", "snack"]):
            cat = "Snacks & Quick Bites"
        elif "burger" in lower:
            cat = "Burgers"

        await ctx.send(sender, card_msg(
            f"🍔 **Campus Canteen Menu: {cat}**:",
            "detail",
            canteen_detail_card(cat)
        ))
        return

    # 4. TIMETABLES HANDLER
    if action == "menu_timetables":
        await ctx.send(sender, card_msg(
            "📅 **RIT Class Timetables: Select your academic year**:",
            "carousel",
            timetables_year_carousel()
        ))
        return

    if action in {"select_year", "view_timetable"} or any(w in lower for w in ["timetable", "schedule", "class", "lecture", "1st year", "2nd year", "3rd year", "4th year"]):
        year_key = action_data.get("year", "1st_year")
        if "2nd" in lower:
            year_key = "2nd_year"
        elif "3rd" in lower:
            year_key = "3rd_year"
        elif "4th" in lower or "final year" in lower:
            year_key = "4th_year"
        elif "1st" in lower:
            year_key = "1st_year"

        day = action_data.get("day", "Monday")
        for d in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]:
            if d in lower:
                day = d.capitalize()
                break

        await ctx.send(sender, card_msg(
            f"📅 **Timetable: {TIMETABLES[year_key]['title']} ({day})**:",
            "detail",
            timetable_detail_card(year_key, day)
        ))
        return

    # 5. BUILDINGS & ROOMS HANDLER
    if action == "menu_buildings" or any(w in lower for w in ["building", "where is", "room", "block b", "block c", "block d", "amenities", "floor"]):
        bldg_id = action_data.get("bldg_id", "")
        if not bldg_id:
            if "block b" in lower or "b-001" in lower or "b-101" in lower:
                bldg_id = "bldg_block_b"
            elif "block c" in lower or "c-202" in lower or "c-212" in lower or "c-306" in lower:
                bldg_id = "bldg_block_c"
            elif "block d" in lower or "d-202" in lower or "placement" in lower:
                bldg_id = "bldg_block_d"
            elif "mess" in lower or "canteen complex" in lower:
                bldg_id = "bldg_amenities"

        if bldg_id:
            await ctx.send(sender, card_msg(
                f"🏛️ **Building Details: {BUILDINGS[bldg_id]['name']}**:",
                "detail",
                building_detail_card(bldg_id)
            ))
            return

        await ctx.send(sender, card_msg(
            "🏛️ **Campus Buildings & Floor Map: Select a building to inspect classrooms and labs**:",
            "carousel",
            buildings_carousel()
        ))
        return

    # 6. FACULTY DIRECTORY HANDLER
    if action == "menu_faculty" or any(w in lower for w in ["faculty", "professor", "teacher", "hod", "lokesh", "atma rai", "himanshu", "deepak arya", "dimpi", "bhanupriya", "priti"]):
        fac_id = action_data.get("faculty_id", "")
        if not fac_id:
            if "lokesh" in lower or "hod" in lower:
                fac_id = "fac_dr_lokesh"
            elif "atma" in lower:
                fac_id = "fac_dr_atma"
            elif "himanshu" in lower:
                fac_id = "fac_himanshu_gupta"
            elif "deepak" in lower:
                fac_id = "fac_deepak_arya"
            elif "dimpi" in lower:
                fac_id = "fac_dimpi_madan"
            elif "bhanupriya" in lower:
                fac_id = "fac_bhanupriya"
            elif "priti" in lower:
                fac_id = "fac_priti_saini"

        if fac_id:
            await ctx.send(sender, card_msg(
                "👨‍🏫 **Faculty Profile & Cabin Details**:",
                "detail",
                faculty_detail_card(fac_id)
            ))
            return

        await ctx.send(sender, card_msg(
            "👨‍🏫 **Faculty & Cabin Directory: Select a faculty member to see visiting hours & subjects**:",
            "carousel",
            faculty_carousel()
        ))
        return

    # Fallback to main menu
    await ctx.send(sender, card_msg(
        "👋 I can help you with timetables, mess food, canteen orders, classrooms, and faculty cabins:",
        "carousel",
        main_menu_carousel()
    ))

@chat_proto.on_message(ChatAcknowledgement)
async def on_ack(ctx: Context, sender: str, msg: ChatAcknowledgement):
    pass

agent.include(chat_proto, publish_manifest=True)

if __name__ == "__main__":
    agent.run()
