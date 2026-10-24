"""
CampusMitra AI - Campus Database
Contains comprehensive Indian campus data:
- Buildings & Classrooms (Floors, Room numbers, Navigation)
- Year-wise & Day-wise Timetables (1st, 2nd, 3rd, 4th Year)
- Faculty Directory (Subjects, Cabin locations, Contact)
"""

# ============================================================================
# 1. CAMPUS BUILDINGS & CLASSROOM DIRECTORY
# ============================================================================
BUILDINGS = {
    "bldg_turing": {
        "id": "bldg_turing",
        "name": "Alan Turing Computer Science Block",
        "code": "CS-BLOCK",
        "total_floors": 4,
        "description": "Houses Computer Science & IT departments, Advanced AI Labs, and Seminar Hall.",
        "icon_url": "https://images.unsplash.com/photo-1562774053-701939374585?w=600",
        "floors": {
            "Ground Floor": ["CS-101 (1st Year CSE)", "CS-102 (1st Year CSE-AI)", "Programming Lab 1", "Server Room"],
            "1st Floor": ["CS-201 (2nd Year CSE-A)", "CS-202 (2nd Year CSE-B)", "Database & Cloud Lab", "HOD Office"],
            "2nd Floor": ["CS-301 (3rd Year CSE-A)", "CS-302 (3rd Year CSE-B)", "AI & Machine Learning Lab", "Faculty Cabins (301-315)"],
            "3rd Floor": ["CS-401 (Final Year Projects)", "CS-402 (Final Year Seminar)", "IoT & Robotics Lab", "Auditorium"]
        }
    },
    "bldg_ramanujan": {
        "id": "bldg_ramanujan",
        "name": "Ramanujan Academic Block",
        "code": "AB-MAIN",
        "total_floors": 3,
        "description": "Main lecture hall complex for 1st Year Foundation Courses, Applied Mathematics, and Physics.",
        "icon_url": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=600",
        "floors": {
            "Ground Floor": ["LT-1 (Lecture Theater 1)", "LT-2 (Lecture Theater 2)", "Student Section Office"],
            "1st Floor": ["Room 201 (1st Year All Branches)", "Room 202 (1st Year ECE)", "Engineering Mechanics Lab"],
            "2nd Floor": ["Room 301 (Mathematics Center)", "Room 302 (Physics Lecture)", "Dean Academics Office"]
        }
    },
    "bldg_ece": {
        "id": "bldg_ece",
        "name": "Vikram Sarabhai Electronics & Tech Block",
        "code": "ECE-BLOCK",
        "total_floors": 3,
        "description": "Electronics, VLSI, Embedded Systems labs, and ECE Department lecture halls.",
        "icon_url": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=600",
        "floors": {
            "Ground Floor": ["EC-101 (1st Year ECE)", "Analog Electronics Lab", "Digital Signal Processing Lab"],
            "1st Floor": ["EC-201 (2nd Year ECE)", "EC-202 (2nd Year ECE)", "VLSI Design Center"],
            "2nd Floor": ["EC-301 (3rd Year ECE)", "EC-401 (Final Year ECE)", "Microwave & Antenna Lab"]
        }
    },
    "bldg_library": {
        "id": "bldg_library",
        "name": "Central Knowledge & Library Complex",
        "code": "CENTRAL-LIB",
        "total_floors": 2,
        "description": "Central Library, Air-conditioned 24/7 Silent Reading Halls, Digital Library, and Group Discussion Rooms.",
        "icon_url": "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=600",
        "floors": {
            "Ground Floor": ["Circulation Counter", "General Stack Room", "Reference Section", "Newspaper Lounge"],
            "1st Floor": ["Silent Study Hall (Capacity: 200)", "Digital Research Lab (50 PCs)", "Group Discussion Rooms A & B"]
        }
    }
}


# ============================================================================
# 2. FACULTY DIRECTORY & SUBJECT ALLOCATION
# ============================================================================
FACULTY_MEMBERS = [
    {
        "id": "fac_sharma",
        "name": "Dr. Rajesh Sharma",
        "designation": "Professor & Head of Department (HOD)",
        "department": "Computer Science & Engineering",
        "subjects": ["Data Structures & Algorithms", "Advanced Algorithms"],
        "cabin": "Turing Block, 1st Floor, Cabin CS-105",
        "email": "rajesh.sharma@campus.edu.in",
        "office_hours": "Mon & Wed: 2:00 PM - 4:00 PM",
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200"
    },
    {
        "id": "fac_verma",
        "name": "Prof. Ananya Verma",
        "designation": "Associate Professor",
        "department": "Computer Science & Engineering",
        "subjects": ["Operating Systems", "System Programming"],
        "cabin": "Turing Block, 2nd Floor, Cabin CS-204",
        "email": "ananya.verma@campus.edu.in",
        "office_hours": "Tue & Thu: 11:00 AM - 1:00 PM",
        "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=200"
    },
    {
        "id": "fac_gupta",
        "name": "Dr. Amit Gupta",
        "designation": "Professor",
        "department": "Computer Science & Engineering",
        "subjects": ["Database Management Systems (DBMS)", "Big Data Analytics"],
        "cabin": "Turing Block, 2nd Floor, Cabin CS-210",
        "email": "amit.gupta@campus.edu.in",
        "office_hours": "Mon & Fri: 3:00 PM - 5:00 PM",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200"
    },
    {
        "id": "fac_kapoor",
        "name": "Prof. Neha Kapoor",
        "designation": "Assistant Professor",
        "department": "Artificial Intelligence & Data Science",
        "subjects": ["Machine Learning", "Artificial Intelligence", "Deep Learning"],
        "cabin": "Turing Block, 3rd Floor, Cabin CS-308",
        "email": "neha.kapoor@campus.edu.in",
        "office_hours": "Wed & Thu: 1:30 PM - 3:30 PM",
        "avatar": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=200"
    },
    {
        "id": "fac_iyer",
        "name": "Dr. S. K. Iyer",
        "designation": "Professor",
        "department": "Applied Sciences & Mathematics",
        "subjects": ["Engineering Mathematics I & II", "Discrete Mathematics"],
        "cabin": "Ramanujan Block, 2nd Floor, Cabin RM-201",
        "email": "sk.iyer@campus.edu.in",
        "office_hours": "Mon, Tue, Fri: 12:00 PM - 1:00 PM",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200"
    },
    {
        "id": "fac_reddy",
        "name": "Dr. P. V. Reddy",
        "designation": "Associate Professor",
        "department": "Electronics & Communication",
        "subjects": ["Digital Signal Processing (DSP)", "Microprocessors & Microcontrollers"],
        "cabin": "Sarabhai ECE Block, 1st Floor, Cabin EC-108",
        "email": "pv.reddy@campus.edu.in",
        "office_hours": "Tue & Thu: 2:00 PM - 4:00 PM",
        "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=200"
    }
]


# ============================================================================
# 3. YEAR-WISE & DAY-WISE TIMETABLES
# ============================================================================
TIMETABLES = {
    # ---------------- 1ST YEAR (FOUNDATION) ----------------
    "1st_year": {
        "title": "1st Year (B.Tech Common Foundation)",
        "classroom": "Ramanujan Block - Lecture Theater 1 (LT-1)",
        "days": {
            "Monday": [
                {"time": "09:00 - 10:00 AM", "subject": "Engineering Mathematics-I", "faculty": "Dr. S. K. Iyer", "room": "LT-1"},
                {"time": "10:00 - 11:00 AM", "subject": "Applied Physics", "faculty": "Dr. Meenakshi Sundaram", "room": "LT-1"},
                {"time": "11:15 - 01:15 PM", "subject": "Physics Laboratory", "faculty": "Physics Dept Staff", "room": "Physics Lab (Ramanujan Gr. Floor)"},
                {"time": "02:00 - 03:00 PM", "subject": "Basic Electrical Engineering", "faculty": "Prof. K. Raman", "room": "LT-1"},
                {"time": "03:00 - 04:00 PM", "subject": "Introduction to Programming (C)", "faculty": "Dr. Rajesh Sharma", "room": "Turing Lab-1"}
            ],
            "Tuesday": [
                {"time": "09:00 - 10:00 AM", "subject": "Engineering Chemistry", "faculty": "Dr. Sunita Rao", "room": "LT-1"},
                {"time": "10:00 - 11:00 AM", "subject": "Engineering Mathematics-I", "faculty": "Dr. S. K. Iyer", "room": "LT-1"},
                {"time": "11:15 - 12:15 PM", "subject": "Professional Communication & Ethics", "faculty": "Prof. Shalini Roy", "room": "LT-1"},
                {"time": "01:00 - 03:00 PM", "subject": "Computer Programming Lab", "faculty": "Dr. Rajesh Sharma", "room": "Turing Lab-1"},
                {"time": "03:15 - 04:15 PM", "subject": "Sports / Library Slot", "faculty": "Library Staff", "room": "Central Library"}
            ],
            "Wednesday": [
                {"time": "09:00 - 10:00 AM", "subject": "Introduction to Programming (C)", "faculty": "Dr. Rajesh Sharma", "room": "LT-1"},
                {"time": "10:00 - 11:00 AM", "subject": "Basic Electrical Engineering", "faculty": "Prof. K. Raman", "room": "LT-1"},
                {"time": "11:15 - 01:15 PM", "subject": "Engineering Drawing & CAD", "faculty": "CAD Instructors", "room": "Drawing Hall (AB-102)"},
                {"time": "02:00 - 03:00 PM", "subject": "Engineering Mathematics-I", "faculty": "Dr. S. K. Iyer", "room": "LT-1"},
                {"time": "03:00 - 04:00 PM", "subject": "Applied Physics Tutorial", "faculty": "Dr. Meenakshi Sundaram", "room": "LT-1"}
            ],
            "Thursday": [
                {"time": "09:00 - 10:00 AM", "subject": "Applied Physics", "faculty": "Dr. Meenakshi Sundaram", "room": "LT-1"},
                {"time": "10:00 - 11:00 AM", "subject": "Engineering Chemistry", "faculty": "Dr. Sunita Rao", "room": "LT-1"},
                {"time": "11:15 - 01:15 PM", "subject": "Electrical Engineering Lab", "faculty": "EE Dept Faculty", "room": "EE Lab-2"},
                {"time": "02:00 - 03:00 PM", "subject": "Basic Electronics", "faculty": "Dr. P. V. Reddy", "room": "LT-1"},
                {"time": "03:00 - 04:00 PM", "subject": "Mentorship & Counseling Session", "faculty": "Faculty Mentors", "room": "LT-1"}
            ],
            "Friday": [
                {"time": "09:00 - 10:00 AM", "subject": "Engineering Mathematics-I", "faculty": "Dr. S. K. Iyer", "room": "LT-1"},
                {"time": "10:00 - 11:00 AM", "subject": "Basic Electronics", "faculty": "Dr. P. V. Reddy", "room": "LT-1"},
                {"time": "11:15 - 12:15 PM", "subject": "Environmental Science", "faculty": "Dr. Sunita Rao", "room": "LT-1"},
                {"time": "01:00 - 03:00 PM", "subject": "Chemistry Laboratory", "faculty": "Chemistry Staff", "room": "Chem Lab (Ramanujan 1st Fl)"},
                {"time": "03:15 - 04:30 PM", "subject": "Student Club & Innovation Hour", "faculty": "Student Council", "room": "Auditorium"}
            ]
        }
    },

    # ---------------- 2ND YEAR (SOPHOMORE) ----------------
    "2nd_year": {
        "title": "2nd Year (Computer Science & Engineering)",
        "classroom": "Turing Block - Room CS-201 (1st Floor)",
        "days": {
            "Monday": [
                {"time": "09:00 - 10:00 AM", "subject": "Data Structures & Algorithms", "faculty": "Dr. Rajesh Sharma", "room": "CS-201"},
                {"time": "10:00 - 11:00 AM", "subject": "Discrete Mathematics", "faculty": "Dr. S. K. Iyer", "room": "CS-201"},
                {"time": "11:15 - 01:15 PM", "subject": "Data Structures Lab (C++/Java)", "faculty": "Dr. Rajesh Sharma & TAs", "room": "Turing Lab-2"},
                {"time": "02:00 - 03:00 PM", "subject": "Digital Logic & Computer Design", "faculty": "Dr. P. V. Reddy", "room": "CS-201"},
                {"time": "03:00 - 04:00 PM", "subject": "Object Oriented Programming (Java)", "faculty": "Prof. Ananya Verma", "room": "CS-201"}
            ],
            "Tuesday": [
                {"time": "09:00 - 10:00 AM", "subject": "Computer Organization & Architecture", "faculty": "Prof. Ananya Verma", "room": "CS-201"},
                {"time": "10:00 - 11:00 AM", "subject": "Data Structures & Algorithms", "faculty": "Dr. Rajesh Sharma", "room": "CS-201"},
                {"time": "11:15 - 12:15 PM", "subject": "Economics for Engineers", "faculty": "Dr. R. K. Mukherjee", "room": "CS-201"},
                {"time": "01:00 - 03:00 PM", "subject": "Java Programming Lab", "faculty": "Prof. Ananya Verma", "room": "Turing Lab-3"},
                {"time": "03:15 - 04:15 PM", "subject": "Discrete Mathematics Tutorial", "faculty": "Dr. S. K. Iyer", "room": "CS-201"}
            ],
            "Wednesday": [
                {"time": "09:00 - 10:00 AM", "subject": "Object Oriented Programming", "faculty": "Prof. Ananya Verma", "room": "CS-201"},
                {"time": "10:00 - 11:00 AM", "subject": "Digital Logic & Computer Design", "faculty": "Dr. P. V. Reddy", "room": "CS-201"},
                {"time": "11:15 - 01:15 PM", "subject": "Digital Electronics Lab", "faculty": "ECE Dept Faculty", "room": "Sarabhai Digital Lab"},
                {"time": "02:00 - 03:00 PM", "subject": "Data Structures & Algorithms", "faculty": "Dr. Rajesh Sharma", "room": "CS-201"},
                {"time": "03:00 - 04:00 PM", "subject": "Competitive Programming & Problem Solving", "faculty": "Coding Club Lead", "room": "Turing Lab-2"}
            ],
            "Thursday": [
                {"time": "09:00 - 10:00 AM", "subject": "Discrete Mathematics", "faculty": "Dr. S. K. Iyer", "room": "CS-201"},
                {"time": "10:00 - 11:00 AM", "subject": "Computer Organization & Architecture", "faculty": "Prof. Ananya Verma", "room": "CS-201"},
                {"time": "11:15 - 12:15 PM", "subject": "Data Structures Practice", "faculty": "Dr. Rajesh Sharma", "room": "CS-201"},
                {"time": "01:00 - 03:00 PM", "subject": "Hardware Simulation Lab", "faculty": "Lab Instructors", "room": "Turing Lab-1"},
                {"time": "03:15 - 04:15 PM", "subject": "Technical Writing & Seminar", "faculty": "Humanities Faculty", "room": "CS-201"}
            ],
            "Friday": [
                {"time": "09:00 - 10:00 AM", "subject": "Digital Logic & Computer Design", "faculty": "Dr. P. V. Reddy", "room": "CS-201"},
                {"time": "10:00 - 11:00 AM", "subject": "Object Oriented Programming", "faculty": "Prof. Ananya Verma", "room": "CS-201"},
                {"time": "11:15 - 12:15 PM", "subject": "Computer Organization Tutorial", "faculty": "Prof. Ananya Verma", "room": "CS-201"},
                {"time": "01:00 - 03:00 PM", "subject": "Mini-Project Work", "faculty": "Project Guides", "room": "Project Lab"},
                {"time": "03:15 - 04:30 PM", "subject": "Hackathon & Industry Workshop", "faculty": "ACM Student Chapter", "room": "Seminar Hall"}
            ]
        }
    },

    # ---------------- 3RD YEAR (JUNIOR) ----------------
    "3rd_year": {
        "title": "3rd Year (Computer Science & Engineering)",
        "classroom": "Turing Block - Room CS-301 (2nd Floor)",
        "days": {
            "Monday": [
                {"time": "09:00 - 10:00 AM", "subject": "Operating Systems", "faculty": "Prof. Ananya Verma", "room": "CS-301"},
                {"time": "10:00 - 11:00 AM", "subject": "Database Management Systems", "faculty": "Dr. Amit Gupta", "room": "CS-301"},
                {"time": "11:15 - 01:15 PM", "subject": "DBMS Laboratory (SQL/PostgreSQL)", "faculty": "Dr. Amit Gupta & TAs", "room": "Database Lab (1st Floor)"},
                {"time": "02:00 - 03:00 PM", "subject": "Machine Learning", "faculty": "Prof. Neha Kapoor", "room": "CS-301"},
                {"time": "03:00 - 04:00 PM", "subject": "Computer Networks", "faculty": "Dr. Suresh Nambiar", "room": "CS-301"}
            ],
            "Tuesday": [
                {"time": "09:00 - 10:00 AM", "subject": "Design & Analysis of Algorithms", "faculty": "Dr. Rajesh Sharma", "room": "CS-301"},
                {"time": "10:00 - 11:00 AM", "subject": "Operating Systems", "faculty": "Prof. Ananya Verma", "room": "CS-301"},
                {"time": "11:15 - 12:15 PM", "subject": "Machine Learning", "faculty": "Prof. Neha Kapoor", "room": "CS-301"},
                {"time": "01:00 - 03:00 PM", "subject": "Operating Systems Lab (Linux/C)", "faculty": "Prof. Ananya Verma", "room": "Turing Lab-2"},
                {"time": "03:15 - 04:15 PM", "subject": "Database Systems Tutorial", "faculty": "Dr. Amit Gupta", "room": "CS-301"}
            ],
            "Wednesday": [
                {"time": "09:00 - 10:00 AM", "subject": "Database Management Systems", "faculty": "Dr. Amit Gupta", "room": "CS-301"},
                {"time": "10:00 - 11:00 AM", "subject": "Computer Networks", "faculty": "Dr. Suresh Nambiar", "room": "CS-301"},
                {"time": "11:15 - 01:15 PM", "subject": "Machine Learning Lab (Python/PyTorch)", "faculty": "Prof. Neha Kapoor", "room": "AI Lab (2nd Floor)"},
                {"time": "02:00 - 03:00 PM", "subject": "Design & Analysis of Algorithms", "faculty": "Dr. Rajesh Sharma", "room": "CS-301"},
                {"time": "03:00 - 04:00 PM", "subject": "Placement Aptitude & Coding Prep", "faculty": "Placement Cell", "room": "CS-301"}
            ],
            "Thursday": [
                {"time": "09:00 - 10:00 AM", "subject": "Machine Learning", "faculty": "Prof. Neha Kapoor", "room": "CS-301"},
                {"time": "10:00 - 11:00 AM", "subject": "Operating Systems", "faculty": "Prof. Ananya Verma", "room": "CS-301"},
                {"time": "11:15 - 12:15 PM", "subject": "Design & Analysis of Algorithms", "faculty": "Dr. Rajesh Sharma", "room": "CS-301"},
                {"time": "01:00 - 03:00 PM", "subject": "Computer Networks Lab (Cisco Packet Tracer)", "faculty": "Dr. Suresh Nambiar", "room": "Network Lab"},
                {"time": "03:15 - 04:15 PM", "subject": "Software Engineering & Agile", "faculty": "Prof. Ritu Saxena", "room": "CS-301"}
            ],
            "Friday": [
                {"time": "09:00 - 10:00 AM", "subject": "Computer Networks", "faculty": "Dr. Suresh Nambiar", "room": "CS-301"},
                {"time": "10:00 - 11:00 AM", "subject": "Database Management Systems", "faculty": "Dr. Amit Gupta", "room": "CS-301"},
                {"time": "11:15 - 12:15 PM", "subject": "Algorithms Problem Solving", "faculty": "Dr. Rajesh Sharma", "room": "CS-301"},
                {"time": "01:00 - 03:00 PM", "subject": "Capstone Project Planning", "faculty": "Faculty Mentors", "room": "Project Lab"},
                {"time": "03:15 - 04:30 PM", "subject": "Guest Lecture / Industry Webinar", "faculty": "Industry Speaker", "room": "Auditorium"}
            ]
        }
    },

    # ---------------- 4TH YEAR (FINAL YEAR) ----------------
    "4th_year": {
        "title": "4th Year (B.Tech Final Year Specialization)",
        "classroom": "Turing Block - Room CS-401 (3rd Floor)",
        "days": {
            "Monday": [
                {"time": "09:00 - 10:00 AM", "subject": "Distributed Systems & Cloud Computing", "faculty": "Dr. Amit Gupta", "room": "CS-401"},
                {"time": "10:00 - 11:00 AM", "subject": "Deep Learning & Generative AI", "faculty": "Prof. Neha Kapoor", "room": "CS-401"},
                {"time": "11:15 - 01:15 PM", "subject": "Cloud & DevOps Lab (AWS/Docker)", "faculty": "Dr. Amit Gupta", "room": "Cloud Lab"},
                {"time": "02:00 - 05:00 PM", "subject": "Major Project-I (Research & Development)", "faculty": "Project Committee", "room": "R&D Lab"}
            ],
            "Tuesday": [
                {"time": "09:00 - 10:00 AM", "subject": "Cybersecurity & Cryptography", "faculty": "Dr. Rajesh Sharma", "room": "CS-401"},
                {"time": "10:00 - 11:00 AM", "subject": "Natural Language Processing (NLP)", "faculty": "Prof. Neha Kapoor", "room": "CS-401"},
                {"time": "11:15 - 01:15 PM", "subject": "Deep Learning Lab (GPU Cluster)", "faculty": "Prof. Neha Kapoor", "room": "AI Supercomputing Lab"},
                {"time": "02:00 - 04:00 PM", "subject": "Industry Internship Reviews", "faculty": "Placement Panel", "room": "Conference Room"}
            ],
            "Wednesday": [
                {"time": "09:00 - 10:00 AM", "subject": "Deep Learning & Generative AI", "faculty": "Prof. Neha Kapoor", "room": "CS-401"},
                {"time": "10:00 - 11:00 AM", "subject": "Distributed Systems & Cloud", "faculty": "Dr. Amit Gupta", "room": "CS-401"},
                {"time": "11:15 - 01:15 PM", "subject": "Cybersecurity & Ethical Hacking Lab", "faculty": "Security Faculty", "room": "Cyber Lab"},
                {"time": "02:00 - 05:00 PM", "subject": "Major Project-I Prototyping", "faculty": "Project Guides", "room": "Project Lab"}
            ],
            "Thursday": [
                {"time": "09:00 - 10:00 AM", "subject": "Cybersecurity & Cryptography", "faculty": "Dr. Rajesh Sharma", "room": "CS-401"},
                {"time": "10:00 - 11:00 AM", "subject": "Natural Language Processing", "faculty": "Prof. Neha Kapoor", "room": "CS-401"},
                {"time": "11:15 - 12:15 PM", "subject": "Entrepreneurship & Startup Incubation", "faculty": "Campus TBI Cell", "room": "CS-401"},
                {"time": "01:00 - 05:00 PM", "subject": "Campus Placement Drives & Tech Interviews", "faculty": "T&P Cell", "room": "Placement Hall"}
            ],
            "Friday": [
                {"time": "09:00 - 11:00 AM", "subject": "Major Project Sprint Review & Demo", "faculty": "Department Evaluation Panel", "room": "Seminar Hall"},
                {"time": "11:15 - 01:15 PM", "subject": "Research Paper Writing & Patent Filing", "faculty": "Dr. Rajesh Sharma", "room": "CS-401"},
                {"time": "02:00 - 04:00 PM", "subject": "Open Source Contributions & Hackathons", "faculty": "Open Source Club", "room": "Turing Lab-3"}
            ]
        }
    }
}


def get_building_by_id(bldg_id: str):
    return BUILDINGS.get(bldg_id)


def get_faculty_by_id(fac_id: str):
    return next((f for f in FACULTY_MEMBERS if f["id"] == fac_id), None)


def search_faculty(query: str):
    q = query.lower()
    results = []
    for f in FACULTY_MEMBERS:
        if q in f["name"].lower() or any(q in s.lower() for s in f["subjects"]) or q in f["department"].lower():
            results.append(f)
    return results


def get_timetable(year_key: str, day: str = "Monday"):
    # Normalize day
    day_norm = day.capitalize()
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
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


def find_room_location(query: str):
    q = query.lower().strip()
    matches = []
    for bldg_id, bldg in BUILDINGS.items():
        for floor, rooms in bldg["floors"].items():
            for r in rooms:
                if q in r.lower():
                    matches.append({
                        "room": r,
                        "floor": floor,
                        "building_name": bldg["name"],
                        "building_code": bldg["code"],
                        "building_id": bldg_id
                    })
    return matches
