"""
CampusMitra AI - Roorkee Institute of Technology (RIT) Campus Database
Includes:
- Official Class Timetables (1st, 2nd, 3rd, 4th Year) with exact timings, subjects, rooms, and faculty
- Official Boys Hostel Mess Menu (Monday - Sunday: Breakfast, Lunch, Tea/Snacks, Dinner)
- Campus Canteen Menu (Burgers, Full Plate Momos, Cold Drinks, Coffee, Cold Coffee, Tea, Snacks)
- Campus Buildings & Classroom Floor Map (Block B, Block C, Block D, Central Library, Central Workshop)
- Faculty Directory with cabin locations and subjects
"""

# ============================================================================
# 1. HOSTEL MESS MENU (OFFICIAL RIT BOYS MESS - MON TO SUN)
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

MESS_NOTES = [
    "First-year students are requested to dine in the first half of meal hours to avoid rush.",
    "Aalo-Paneer Mix Bhurji uses 25 kg pure paneer for hostel residents.",
    "3 kg pure Desi Ghee is served fresh on chapatis during Lunch and 3 kg for Dinner daily.",
    "Fresh green salad contains cucumber, radish (muli), tomato, carrot & onion.",
    "Seasonal fruit: Watermelon and Mangoes served during summer months (May-June)."
]


# ============================================================================
# 2. CAMPUS CANTEEN MENU
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
# 3. CAMPUS BUILDINGS & CLASSROOMS DIRECTORY (RIT CAMPUS)
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
            ],
            "3rd Floor": [
                {"room": "B-301", "name": "1st Year ME/CE/EE Section J Classroom", "capacity": 70, "type": "Classroom"}
            ]
        }
    },
    "bldg_block_c": {
        "id": "bldg_block_c",
        "name": "Academic Block C (Core CSE & IT)",
        "code": "BLOCK-C",
        "total_floors": 4,
        "description": "Center for 2nd Year, 3rd Year CSE, CSE-AIML, HOD CSE Office, and Advanced Computer Labs.",
        "icon_url": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=600",
        "floors": {
            "Ground Floor": [
                {"room": "C-002", "name": "1st Year CSE Section D Classroom", "capacity": 75, "type": "Classroom"},
                {"room": "C-004", "name": "1st Year CSE Section E Classroom", "capacity": 75, "type": "Classroom"},
                {"room": "C-012", "name": "Computing Lab & Digital Electronics Lab", "capacity": 60, "type": "Lab"},
                {"room": "C-015", "name": "Basic Electrical Engineering Lab (EEP-001)", "capacity": 60, "type": "Hardware Lab"}
            ],
            "1st Floor": [
                {"room": "C-108", "name": "1st Year CSE-AIML Section F", "capacity": 70, "type": "Classroom"},
                {"room": "C-112", "name": "1st Year CSE-AIML Section G", "capacity": 70, "type": "Classroom"},
                {"room": "C-114", "name": "1st Year CSE-AIML Section H", "capacity": 70, "type": "Classroom"},
                {"room": "C-116", "name": "1st Year ECE Section I Classroom", "capacity": 70, "type": "Classroom"},
                {"room": "C-113", "name": "Basic Mechanical Engineering Lab (MEP-001)", "capacity": 50, "type": "Workshop Lab"}
            ],
            "2nd Floor": [
                {"room": "C-202", "name": "2nd Year CSE Section IIA-A (Smart Classroom)", "capacity": 75, "type": "Classroom"},
                {"room": "C-204", "name": "2nd Year CSE Section IIA-B", "capacity": 75, "type": "Classroom"},
                {"room": "C-206", "name": "2nd Year CSE Section IIA-C", "capacity": 75, "type": "Classroom"},
                {"room": "C-208", "name": "2nd Year CSE Section IIA-D", "capacity": 75, "type": "Classroom"},
                {"room": "C-210", "name": "2nd Year CSE Section IIA-E", "capacity": 75, "type": "Classroom"},
                {"room": "C-212", "name": "3rd Year CSE Section IIIA-A", "capacity": 75, "type": "Classroom"},
                {"room": "C-214", "name": "3rd Year CSE Section IIIA-B", "capacity": 75, "type": "Classroom"},
                {"room": "C-216", "name": "3rd Year CSE Section IIIA-C", "capacity": 75, "type": "Classroom"}
            ],
            "3rd Floor": [
                {"room": "C-305", "name": "3rd Year CSE Section IIIA-D", "capacity": 75, "type": "Classroom"},
                {"room": "C-306", "name": "2nd Year CSE (AIML) Section A", "capacity": 75, "type": "Classroom"},
                {"room": "C-310", "name": "Engineering Graphics & Design Lab (MEP-002)", "capacity": 60, "type": "CAD Studio"}
            ]
        }
    },
    "bldg_block_d": {
        "id": "bldg_block_d",
        "name": "Academic Block D (Final Year & Research)",
        "code": "BLOCK-D",
        "total_floors": 3,
        "description": "Houses B.Tech 4th Year Specialization (Room D-202), AI Project Labs, Seminar Halls, and Dean Academics.",
        "icon_url": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=600",
        "floors": {
            "Ground Floor": [
                {"room": "D-001", "name": "Student Training & Placement Cell (T&P)", "capacity": 40, "type": "Admin"},
                {"room": "D-002", "name": "Corporate Interview Rooms", "capacity": 30, "type": "Interview"}
            ],
            "1st Floor": [
                {"room": "D-101", "name": "Dean Academics & Administrative Chambers", "capacity": 20, "type": "Admin"},
                {"room": "D-102", "name": "Faculty Conference Room", "capacity": 40, "type": "Conference"}
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
# 4. OFFICIAL TIMETABLES (1ST, 2ND, 3RD, 4TH YEAR) - MONDAY TO SATURDAY
# ============================================================================
TIMETABLES = {
    # ---------------- 1ST YEAR (B.TECH CSE SEC A - ROOM B-001) ----------------
    "1st_year": {
        "title": "1st Year (B.Tech CSE Section A)",
        "classroom": "Block B - Room B-001",
        "days": {
            "Monday": [
                {"time": "09:05 - 09:55 AM", "subject": "Engineering Mathematics-I (AHT-003)", "faculty": "Dr. S. K. Iyer (SK)", "room": "B-001"},
                {"time": "09:55 - 10:45 AM", "subject": "Programming for Problem Solving (CST-001)", "faculty": "Mr. Gaurav Chaturvedi (GC)", "room": "B-001"},
                {"time": "11:05 - 01:15 PM", "subject": "Physics Lab (AHP-001) / Electrical Lab (EEP-001)", "faculty": "Dr. Atma Rai (AR) / Mr. Ankit Mainwal (AM)", "room": "B-101 / C-015"},
                {"time": "01:45 - 02:35 PM", "subject": "Basic Electrical Engineering (EET-001)", "faculty": "Mr. Ankit Mainwal (AM)", "room": "B-001"},
                {"time": "02:35 - 03:25 PM", "subject": "Self Employment & Entrepreneurship (AHP-005)", "faculty": "Mr. Abhishek Jain (AJ)", "room": "B-001"}
            ],
            "Tuesday": [
                {"time": "09:05 - 09:55 AM", "subject": "Engineering Mathematics-I (AHT-003)", "faculty": "Dr. S. K. Iyer (SK)", "room": "B-001"},
                {"time": "09:55 - 10:45 AM", "subject": "Programming for Problem Solving (CST-001)", "faculty": "Mr. Gaurav Chaturvedi (GC)", "room": "B-001"},
                {"time": "11:05 - 11:55 AM", "subject": "Engineering Physics (AHT-001)", "faculty": "Dr. Atma Rai (AR)", "room": "B-001"},
                {"time": "11:55 - 12:45 PM", "subject": "Engineering Graphics Tutorial (MEP-002)", "faculty": "Mr. Narendra Bansal (NB)", "room": "B-001"},
                {"time": "01:45 - 03:25 PM", "subject": "Digital Marketing Lab (AHP-003)", "faculty": "Mr. Harsh Dharia (HD)", "room": "B-105"}
            ],
            "Wednesday": [
                {"time": "09:05 - 09:55 AM", "subject": "Engineering Mathematics-I (AHT-003)", "faculty": "Dr. S. K. Iyer (SK)", "room": "B-001"},
                {"time": "09:55 - 10:45 AM", "subject": "Programming for Problem Solving (CST-001)", "faculty": "Mr. Gaurav Chaturvedi (GC)", "room": "B-001"},
                {"time": "11:05 - 11:55 AM", "subject": "Programming for Problem Solving (CST-001)", "faculty": "Mr. Gaurav Chaturvedi (GC)", "room": "B-001"},
                {"time": "11:55 - 12:45 PM", "subject": "Basic Electrical Engineering (EET-001)", "faculty": "Mr. Ankit Mainwal (AM)", "room": "B-001"},
                {"time": "01:45 - 03:25 PM", "subject": "Engineering Graphics & Design (MEP-002) / C Programming Lab (CSP-001)", "faculty": "Mr. Narendra Bansal / Dr. Neeraj Kumar", "room": "C-310 / A-101"}
            ],
            "Thursday": [
                {"time": "09:05 - 09:55 AM", "subject": "Engineering Mathematics-I (AHT-003)", "faculty": "Dr. S. K. Iyer (SK)", "room": "B-001"},
                {"time": "09:55 - 10:45 AM", "subject": "Programming for Problem Solving (CST-001)", "faculty": "Mr. Gaurav Chaturvedi (GC)", "room": "B-001"},
                {"time": "11:05 - 11:55 AM", "subject": "Engineering Physics (AHT-001)", "faculty": "Dr. Atma Rai (AR)", "room": "B-001"},
                {"time": "11:55 - 12:45 PM", "subject": "Basic Electrical Engineering (EET-001)", "faculty": "Mr. Ankit Mainwal (AM)", "room": "B-001"},
                {"time": "01:45 - 03:25 PM", "subject": "Engineering Physics Lab (AHP-001) / Electrical Lab (EEP-001)", "faculty": "Dr. Atma Rai / Mr. Ankit Mainwal", "room": "B-101 / C-015"}
            ],
            "Friday": [
                {"time": "09:05 - 09:55 AM", "subject": "Graphics Lab (MEP-002) / C Programming Lab (CSP-001)", "faculty": "Mr. Narendra Bansal / Dr. Neeraj Kumar", "room": "C-310 / A-101"},
                {"time": "11:05 - 11:55 AM", "subject": "Engineering Physics (AHT-001)", "faculty": "Dr. Atma Rai (AR)", "room": "B-001"},
                {"time": "11:55 - 12:45 PM", "subject": "Basic Electrical Engineering (EET-001)", "faculty": "Mr. Ankit Mainwal (AM)", "room": "B-001"},
                {"time": "01:45 - 02:35 PM", "subject": "Environmental Studies (AHT-004)", "faculty": "Dr. Sandeep Joshi (SJ)", "room": "B-001"},
                {"time": "02:35 - 03:25 PM", "subject": "Self Employment & Entrepreneurship (AHP-005)", "faculty": "Mr. Abhishek Jain (AJ)", "room": "B-001"}
            ],
            "Saturday": [
                {"time": "09:05 - 09:55 AM", "subject": "Engineering Mathematics-I Tutorial (AHT-003)", "faculty": "Dr. S. K. Iyer (SK)", "room": "B-001"},
                {"time": "09:55 - 10:45 AM", "subject": "Programming Tutorial (CST-001)", "faculty": "Mr. Gaurav Chaturvedi (GC)", "room": "B-001"},
                {"time": "11:05 - 11:55 AM", "subject": "Engineering Physics Tutorial (AHT-001)", "faculty": "Dr. Atma Rai (AR)", "room": "B-001"},
                {"time": "11:55 - 12:45 PM", "subject": "Electrical Engineering Tutorial (EET-001)", "faculty": "Mr. Ankit Mainwal (AM)", "room": "B-001"},
                {"time": "01:45 - 02:35 PM", "subject": "Environmental Studies (AHT-004)", "faculty": "Dr. Sandeep Joshi (SJ)", "room": "B-001"},
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
                {"time": "09:05 - 09:55 AM", "subject": "Object Oriented Programming (CST-004)", "faculty": "Ms. Dimpi Madan (DP)", "room": "C-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Universal Human Values (AHT-008)", "faculty": "Dr. Rashmi Gupta (RG)", "room": "C-202"},
                {"time": "11:05 - 11:55 AM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-202"},
                {"time": "11:55 - 12:45 PM", "subject": "OOPs Lab (CSP-004) / DSA Lab (CSP-003)", "faculty": "Ms. Dimpi Madan / Dr. Himanshu Gupta", "room": "B-208 / B-206"},
                {"time": "01:45 - 04:15 PM", "subject": "GeeksforGeeks (GFG) Elite / Regular Coding", "faculty": "Coding Mentors", "room": "C-202 / C-204"}
            ],
            "Tuesday": [
                {"time": "09:05 - 09:55 AM", "subject": "Discrete Structure (CST-002)", "faculty": "Dr. Akshay Saini (AKS)", "room": "C-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Object Oriented Programming (CST-004)", "faculty": "Ms. Dimpi Madan (DP)", "room": "C-202"},
                {"time": "11:05 - 11:55 AM", "subject": "Data Structures & Algorithms (CST-003)", "faculty": "Dr. Himanshu Gupta (HG)", "room": "C-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Object Oriented Programming (CST-004)", "faculty": "Ms. Dimpi Madan (DP)", "room": "C-202"},
                {"time": "01:45 - 04:15 PM", "subject": "GeeksforGeeks (GFG) Elite Problem Solving", "faculty": "Coding Mentors", "room": "C-202 / C-204"}
            ],
            "Wednesday": [
                {"time": "09:05 - 09:55 AM", "subject": "Universal Human Values (AHT-008)", "faculty": "Dr. Rashmi Gupta (RG)", "room": "C-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Data Structures & Algorithms (CST-003)", "faculty": "Dr. Himanshu Gupta (HG)", "room": "C-202"},
                {"time": "11:05 - 11:55 AM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Digital Electronics (ECT-033)", "faculty": "Dr. Ranjan Mishra (RM)", "room": "C-202"},
                {"time": "01:45 - 04:15 PM", "subject": "GeeksforGeeks (GFG) Competitive Coding", "faculty": "Coding Mentors", "room": "C-202 / C-204"}
            ],
            "Thursday": [
                {"time": "09:05 - 09:55 AM", "subject": "Python Programming (CST-005)", "faculty": "Dr. Deepak Arya (DA)", "room": "C-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Digital Electronics (ECT-033)", "faculty": "Dr. Ranjan Mishra (RM)", "room": "C-202"},
                {"time": "11:05 - 11:55 AM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Discrete Structure (CST-002)", "faculty": "Dr. Akshay Saini (AKS)", "room": "C-202"},
                {"time": "01:45 - 04:15 PM", "subject": "GeeksforGeeks (GFG) Elite Coding Practice", "faculty": "Coding Mentors", "room": "C-202 / C-204"}
            ],
            "Friday": [
                {"time": "09:05 - 09:55 AM", "subject": "OOPs Lab (CSP-004) / Python Lab (CSP-005)", "faculty": "Ms. Dimpi Madan / Dr. Deepak Arya", "room": "B-106 / B-207"},
                {"time": "09:55 - 10:45 AM", "subject": "Data Structures & Algorithms (CST-003)", "faculty": "Dr. Himanshu Gupta (HG)", "room": "C-202"},
                {"time": "11:05 - 11:55 AM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Data Structures & Algorithms (CST-003)", "faculty": "Dr. Himanshu Gupta (HG)", "room": "C-202"},
                {"time": "01:45 - 04:15 PM", "subject": "GeeksforGeeks (GFG) Elite Coding", "faculty": "Coding Mentors", "room": "C-202 / C-204"}
            ],
            "Saturday": [
                {"time": "09:05 - 09:55 AM", "subject": "Digital Electronics (ECT-033)", "faculty": "Dr. Ranjan Mishra (RM)", "room": "C-202"},
                {"time": "09:55 - 10:45 AM", "subject": "DSA Lab (CSP-003) / Python Lab (CSP-005)", "faculty": "Dr. Himanshu Gupta / Dr. Deepak Arya", "room": "B-208 / B-207"},
                {"time": "11:05 - 11:55 AM", "subject": "Discrete Structure (CST-002)", "faculty": "Dr. Akshay Saini (AKS)", "room": "C-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Object Oriented Programming (CST-004)", "faculty": "Ms. Dimpi Madan (DP)", "room": "C-202"},
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
                {"time": "11:05 - 11:55 AM", "subject": "Compiler Design (CST-012)", "faculty": "Ms. Bhanupriya (BP)", "room": "C-212"},
                {"time": "11:55 - 12:45 PM", "subject": "Software Engineering (CST-015)", "faculty": "Ms. Chandani (CH)", "room": "C-212"},
                {"time": "01:45 - 03:25 PM", "subject": "DBMS Lab (CSP-011) / Compiler Lab (CSP-012)", "faculty": "Ms. Priti Saini / Ms. Bhanupriya", "room": "C-012 / B-105"},
                {"time": "03:25 - 04:15 PM", "subject": "Design & Analysis of Algorithms (CST-010)", "faculty": "Mr. Vipin Jaiswal (VJ)", "room": "C-212"},
                {"time": "04:15 - 05:00 PM", "subject": "Database Management Systems (CST-011)", "faculty": "Ms. Priti Saini (PS)", "room": "C-212"}
            ],
            "Tuesday": [
                {"time": "09:05 - 10:45 AM", "subject": "GeeksforGeeks (GFG) Regular/Elite Track", "faculty": "GFG Mentors", "room": "C-212 / C-214"},
                {"time": "11:05 - 11:55 AM", "subject": "Compiler Design (CST-012)", "faculty": "Ms. Bhanupriya (BP)", "room": "C-212"},
                {"time": "11:55 - 12:45 PM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-212"},
                {"time": "01:45 - 02:35 PM", "subject": "Distributed Systems (CST-019)", "faculty": "Dr. Abhay Bhatia (AB)", "room": "C-212"},
                {"time": "02:35 - 03:25 PM", "subject": "Design & Analysis of Algorithms (CST-010)", "faculty": "Mr. Vipin Jaiswal (VJ)", "room": "C-212"},
                {"time": "03:25 - 05:00 PM", "subject": "DBMS Lab (CSP-011) / DAA Lab (CSP-010)", "faculty": "Ms. Priti Saini / Mr. Vipin Jaiswal", "room": "C-012 / B-106"}
            ],
            "Wednesday": [
                {"time": "09:05 - 10:45 AM", "subject": "GeeksforGeeks (GFG) Regular/Elite Track", "faculty": "GFG Mentors", "room": "C-212 / C-214"},
                {"time": "11:05 - 11:55 AM", "subject": "Compiler Design (CST-012)", "faculty": "Ms. Bhanupriya (BP)", "room": "C-212"},
                {"time": "11:55 - 12:45 PM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-212"},
                {"time": "01:45 - 02:35 PM", "subject": "Database Management Systems (CST-011)", "faculty": "Ms. Priti Saini (PS)", "room": "C-212"},
                {"time": "02:35 - 03:25 PM", "subject": "Design & Analysis of Algorithms (CST-010)", "faculty": "Mr. Vipin Jaiswal (VJ)", "room": "C-212"},
                {"time": "03:25 - 04:15 PM", "subject": "Distributed Systems (CST-019)", "faculty": "Dr. Abhay Bhatia (AB)", "room": "C-212"},
                {"time": "04:15 - 05:00 PM", "subject": "Software Engineering (CST-015)", "faculty": "Ms. Chandani (CH)", "room": "C-212"}
            ],
            "Thursday": [
                {"time": "09:05 - 10:45 AM", "subject": "GeeksforGeeks (GFG) Problem Solving Track", "faculty": "GFG Mentors", "room": "C-212 / C-214"},
                {"time": "11:05 - 11:55 AM", "subject": "Design & Analysis of Algorithms (CST-010)", "faculty": "Mr. Vipin Jaiswal (VJ)", "room": "C-212"},
                {"time": "11:55 - 12:45 PM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-212"},
                {"time": "01:45 - 02:35 PM", "subject": "Compiler Design (CST-012)", "faculty": "Ms. Bhanupriya (BP)", "room": "C-212"},
                {"time": "02:35 - 03:25 PM", "subject": "Database Management Systems (CST-011)", "faculty": "Ms. Priti Saini (PS)", "room": "C-212"},
                {"time": "03:25 - 05:00 PM", "subject": "DAA Lab (CSP-010) / Compiler Lab (CSP-012)", "faculty": "Mr. Vipin Jaiswal / Ms. Bhanupriya", "room": "B-106 / B-208"}
            ],
            "Friday": [
                {"time": "09:05 - 10:45 AM", "subject": "GeeksforGeeks (GFG) Coding Contest", "faculty": "GFG Mentors", "room": "C-212 / C-214"},
                {"time": "11:05 - 11:55 AM", "subject": "Constitution of India (AHT-009)", "faculty": "Mr. Rao Ragib Khan (RRK)", "room": "C-212"},
                {"time": "11:55 - 12:45 PM", "subject": "IBM Corporate Training", "faculty": "Mr. Adarsh (IBM)", "room": "C-212"},
                {"time": "01:45 - 02:35 PM", "subject": "Distributed Systems (CST-019)", "faculty": "Dr. Abhay Bhatia (AB)", "room": "C-212"},
                {"time": "02:35 - 03:25 PM", "subject": "Software Engineering (CST-015)", "faculty": "Ms. Chandani (CH)", "room": "C-212"},
                {"time": "03:25 - 04:15 PM", "subject": "Database Management Systems (CST-011)", "faculty": "Ms. Priti Saini (PS)", "room": "C-212"}
            ],
            "Saturday": [
                {"time": "09:05 - 10:45 AM", "subject": "GeeksforGeeks (GFG) Weekly Sprint", "faculty": "GFG Mentors", "room": "C-212 / C-214"},
                {"time": "11:05 - 11:55 AM", "subject": "Database Management Systems (CST-011)", "faculty": "Ms. Priti Saini (PS)", "room": "C-212"},
                {"time": "11:55 - 12:45 PM", "subject": "Design & Analysis of Algorithms (CST-010)", "faculty": "Mr. Vipin Jaiswal (VJ)", "room": "C-212"},
                {"time": "01:45 - 02:35 PM", "subject": "Distributed Systems (CST-019)", "faculty": "Dr. Abhay Bhatia (AB)", "room": "C-212"},
                {"time": "02:35 - 03:25 PM", "subject": "Software Engineering (CST-015)", "faculty": "Ms. Chandani (CH)", "room": "C-212"},
                {"time": "03:25 - 04:15 PM", "subject": "Compiler Design (CST-012)", "faculty": "Ms. Bhanupriya (BP)", "room": "C-212"}
            ]
        }
    },

    # ---------------- 4TH YEAR (B.TECH CSE FINAL YEAR - ROOM D-202) ----------------
    "4th_year": {
        "title": "4th Year (B.Tech CSE Final Year Specialization)",
        "classroom": "Block D - Room D-202 (2nd Floor)",
        "days": {
            "Monday": [
                {"time": "09:05 - 09:55 AM", "subject": "Cloud Computing (CST-037)", "faculty": "Ms. Bhanupriya (BP)", "room": "D-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Machine Learning (CST-030)", "faculty": "Dr. Gaurav Kumar (GK)", "room": "D-202"},
                {"time": "11:05 - 11:55 AM", "subject": "Advanced Mobile Technology (EEC-066)", "faculty": "Ms. Priti Saini (PS)", "room": "D-202"},
                {"time": "01:45 - 02:35 PM", "subject": "Disaster Management (AHT-017)", "faculty": "Dr. Anil Chauhan (ACH)", "room": "D-202"},
                {"time": "02:35 - 04:15 PM", "subject": "Major Capstone Project Seminar (CSP-018)", "faculty": "Mr. Avnish Chauhan (AV)", "room": "D-202 / R&D Lab"}
            ],
            "Tuesday": [
                {"time": "09:05 - 09:55 AM", "subject": "Disaster Management (AHT-017)", "faculty": "Dr. Anil Chauhan (ACH)", "room": "D-202"},
                {"time": "11:05 - 11:55 AM", "subject": "Advanced Mobile Technology (EEC-066)", "faculty": "Ms. Priti Saini (PS)", "room": "D-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Cloud Computing (CST-037)", "faculty": "Ms. Bhanupriya (BP)", "room": "D-202"},
                {"time": "01:45 - 02:35 PM", "subject": "Disaster Management (AHT-017)", "faculty": "Mr. Deepak Kumar (DK)", "room": "D-202"},
                {"time": "02:35 - 05:00 PM", "subject": "Industry Placement Mock Interviews & Drives", "faculty": "T&P Cell", "room": "Placement Hall"}
            ],
            "Wednesday": [
                {"time": "09:05 - 09:55 AM", "subject": "Disaster Management (AHT-017)", "faculty": "Dr. Anil Chauhan (ACH)", "room": "D-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Advanced Mobile Technology (EEC-066)", "faculty": "Ms. Priti Saini (PS)", "room": "D-202"},
                {"time": "11:05 - 11:55 AM", "subject": "Innovations & Problem Solving (AHT-018)", "faculty": "Ms. Taniya Dhiman (TD)", "room": "D-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Machine Learning (CST-030)", "faculty": "Dr. Gaurav Kumar (GK)", "room": "D-202"},
                {"time": "01:45 - 02:35 PM", "subject": "Rural Development & Administration (AHT-015)", "faculty": "Mr. Deepak Kumar (DK)", "room": "D-202"},
                {"time": "02:35 - 04:15 PM", "subject": "Major Design Project Prototyping (CSP-019)", "faculty": "Ms. Bhanupriya (BP)", "room": "Project Lab"}
            ],
            "Thursday": [
                {"time": "09:05 - 09:55 AM", "subject": "Cloud Computing (CST-037)", "faculty": "Ms. Bhanupriya (BP)", "room": "D-202"},
                {"time": "11:05 - 11:55 AM", "subject": "Innovations & Problem Solving (AHT-018)", "faculty": "Ms. Taniya Dhiman (TD)", "room": "D-202"},
                {"time": "11:55 - 12:45 PM", "subject": "Disaster Management (AHT-017)", "faculty": "Dr. Anil Chauhan (ACH)", "room": "D-202"},
                {"time": "01:45 - 03:25 PM", "subject": "Machine Learning Lab & GPU Experiments", "faculty": "Dr. Gaurav Kumar", "room": "AI Lab"},
                {"time": "03:25 - 05:00 PM", "subject": "Startup Pitch & Incubation Reviews", "faculty": "Dean Incubation", "room": "Conference Room"}
            ],
            "Friday": [
                {"time": "09:05 - 09:55 AM", "subject": "Machine Learning (CST-030)", "faculty": "Dr. Gaurav Kumar (GK)", "room": "D-202"},
                {"time": "09:55 - 10:45 AM", "subject": "Cloud Computing Architecture (CST-037)", "faculty": "Ms. Bhanupriya (BP)", "room": "D-202"},
                {"time": "11:05 - 12:45 PM", "subject": "Design Project Lab & Sprint Demo (CSP-019)", "faculty": "Ms. Bhanupriya (BP)", "room": "Project Lab"},
                {"time": "01:45 - 04:15 PM", "subject": "Open Source Contributions & Research Paper Writing", "faculty": "Research Committee", "room": "D-202"}
            ],
            "Saturday": [
                {"time": "09:05 - 11:00 AM", "subject": "Capstone Major Project Presentation & Review", "faculty": "Department Evaluation Panel", "room": "D-202 / Seminar Hall"},
                {"time": "11:15 - 01:15 PM", "subject": "Patent Filing, Ethics & Research Documentation", "faculty": "Dr. Lokesh Kumar (HOD)", "room": "D-202"},
                {"time": "02:00 - 04:00 PM", "subject": "Alumni Mentorship & Placement Preparations", "faculty": "Alumni Relations", "room": "Auditorium"}
            ]
        }
    }
}


# ============================================================================
# 5. FACULTY DIRECTORY (RIT ROORKEE)
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
        "subjects": ["Object Oriented Programming (CST-004)", "OOPs Lab (CSP-004)"],
        "cabin": "Block C, 2nd Floor, Cabin C-203",
        "email": "dimpi.madan@ritroorkee.com",
        "office_hours": "Monday & Thursday: 10:00 AM - 12:00 PM",
        "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200"
    },
    {
        "id": "fac_ranjan_mishra",
        "name": "Dr. Ranjan Mishra",
        "designation": "Professor",
        "department": "Electronics & Electrical",
        "subjects": ["Digital Electronics (ECT-033)", "Microprocessor Systems"],
        "cabin": "Block C, 1st Floor, Cabin C-105",
        "email": "ranjan.mishra@ritroorkee.com",
        "office_hours": "Tuesday & Thursday: 2:00 PM - 4:00 PM",
        "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=200"
    },
    {
        "id": "fac_bhanupriya",
        "name": "Ms. Bhanupriya",
        "designation": "Assistant Professor",
        "department": "Computer Science & Engineering",
        "subjects": ["Compiler Design (CST-012)", "Cloud Computing (CST-037)", "Design Project (CSP-019)"],
        "cabin": "Block C, 2nd Floor, Cabin C-215",
        "email": "bhanupriya@ritroorkee.com",
        "office_hours": "Monday & Friday: 1:30 PM - 3:30 PM",
        "avatar": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=200"
    },
    {
        "id": "fac_vipin_jaiswal",
        "name": "Mr. Vipin Jaiswal",
        "designation": "Assistant Professor",
        "department": "Computer Science & Engineering",
        "subjects": ["Design and Analysis of Algorithm (CST-010)", "DAA Lab (CSP-010)"],
        "cabin": "Block C, 2nd Floor, Cabin C-211",
        "email": "vipin.jaiswal@ritroorkee.com",
        "office_hours": "Wednesday & Thursday: 3:00 PM - 5:00 PM",
        "avatar": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=200"
    },
    {
        "id": "fac_priti_saini",
        "name": "Ms. Priti Saini",
        "designation": "Assistant Professor",
        "department": "Computer Science & Engineering",
        "subjects": ["Database Management System (CST-011)", "Advanced Mobile Technology (EEC-066)"],
        "cabin": "Block C, 2nd Floor, Cabin C-213",
        "email": "priti.saini@ritroorkee.com",
        "office_hours": "Tuesday & Friday: 11:00 AM - 1:00 PM",
        "avatar": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=200"
    },
    {
        "id": "fac_gaurav_kumar",
        "name": "Dr. Gaurav Kumar",
        "designation": "Associate Professor",
        "department": "Computer Science & Engineering",
        "subjects": ["Machine Learning (CST-030)", "Python Programming (CST-005)"],
        "cabin": "Block D, 2nd Floor, Cabin D-205",
        "email": "gaurav.kumar@ritroorkee.com",
        "office_hours": "Monday & Thursday: 2:00 PM - 4:00 PM",
        "avatar": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=200"
    }
]


# ============================================================================
# 6. QUERY HELPERS
# ============================================================================
def get_all_buildings():
    return list(BUILDINGS.values())

def get_building_by_id(bldg_id: str):
    return BUILDINGS.get(bldg_id)

def get_all_faculty():
    return FACULTY_MEMBERS

def get_faculty_by_id(fac_id: str):
    return next((f for f in FACULTY_MEMBERS if f["id"] == fac_id), None)

def search_faculty(query: str):
    q = query.lower().strip()
    results = []
    for f in FACULTY_MEMBERS:
        if (q in f["name"].lower() or 
            any(q in s.lower() for s in f["subjects"]) or 
            q in f["department"].lower() or
            q in f["cabin"].lower()):
            results.append(f)
    return results

def get_timetable(year_key: str, day: str = "Monday"):
    day_norm = day.capitalize()
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if day_norm not in valid_days:
        day_norm = "Monday"

    year_data = TIMETABLES.get(year_key, TIMETABLES["1st_year"])
    day_schedule = year_data["days"].get(day_norm, year_data["days"]["Monday"])
    return {
        "year_key": year_key,
        "title": year_data["title"],
        "classroom": year_data["classroom"],
        "day": day_norm,
        "schedule": day_schedule
    }

def get_mess_menu(day: str = "Monday"):
    day_norm = day.capitalize()
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day_norm not in valid_days:
        day_norm = "Monday"

    day_food = MESS_MENU.get(day_norm, MESS_MENU["Monday"])
    return {
        "day": day_norm,
        "timings": MESS_TIMINGS,
        "meals": day_food,
        "notes": MESS_NOTES
    }

def get_canteen_menu():
    return CANTEEN_MENU

def find_room_location(query: str):
    q = query.lower().strip()
    matches = []
    for bldg_id, bldg in BUILDINGS.items():
        for floor, rooms in bldg["floors"].items():
            for r in rooms:
                if (q in r["room"].lower() or 
                    q in r["name"].lower() or 
                    any(part in r["room"].lower() for part in q.split())):
                    matches.append({
                        "room_code": r["room"],
                        "room_name": r["name"],
                        "room_type": r.get("type", "Room"),
                        "floor": floor,
                        "building_name": bldg["name"],
                        "building_code": bldg["code"],
                        "building_id": bldg_id
                    })
    return matches
