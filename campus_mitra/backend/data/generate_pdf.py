"""
Generate comprehensive RIT campus_handbook.pdf using reportlab for RAG extraction.
Includes Mess Menu, Canteen Menu, All 4 Years Timetables, and Faculty Directory.
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

output_pdf = os.path.join(os.path.dirname(__file__), "campus_handbook.pdf")
doc = SimpleDocTemplate(output_pdf, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Heading1'],
    fontSize=18,
    leading=22,
    textColor=colors.HexColor('#1E3A8A'),
    alignment=1
)

h1_style = ParagraphStyle(
    'SectionH1',
    parent=styles['Heading2'],
    fontSize=12,
    leading=16,
    textColor=colors.HexColor('#1E40AF'),
    spaceBefore=10,
    spaceAfter=4
)

body_style = ParagraphStyle(
    'BodyDark',
    parent=styles['Normal'],
    fontSize=9,
    leading=12,
    textColor=colors.HexColor('#1F2937')
)

story = []

# Title
story.append(Paragraph("ROORKEE INSTITUTE OF TECHNOLOGY (RIT)", title_style))
story.append(Paragraph("CampusMitra AI - Official Student Handbook, Mess & Canteen Guide (2026-2027)", ParagraphStyle('Sub', parent=body_style, alignment=1, textColor=colors.HexColor('#4B5563'))))
story.append(Spacer(1, 10))

# 1. Mess Menu
story.append(Paragraph("1. Boys Hostel Mess Menu & Meal Timings", h1_style))
story.append(Paragraph("<b>Timings:</b> Breakfast: 07:30 AM - 08:30 AM | Lunch: 12:45 PM - 01:45 PM | Tea/Snacks: 05:15 PM - 06:00 PM | Dinner: 08:00 PM - 09:00 PM", body_style))
story.append(Paragraph("• <b>Monday:</b> Breakfast: Aloo Paratha, Dahi, Packed Butter, Tea, Banana. Lunch: Dal Arhar, Bhindi / Aloo Gobhi, Rice, Chapati, Salad, Papad. Tea: Bread Pakoda, Tea. Dinner: Dal Urad Channa, Shahi Paneer, Rice, Chapati, Sweet Dish (Kheer).", body_style))
story.append(Paragraph("• <b>Tuesday:</b> Breakfast: Pav Bhaji, Apple, Milk / Tea. Lunch: Peas Pulao, Rajma, Chutney, Dahi Bhalla, Chapati, Salad, Papad. Tea: Mix Veg Noodles, Tea. Dinner: Dal Arhar, Mix Veg, Rice, Chapati, Sweet Dish (Hot Jalebi).", body_style))
story.append(Paragraph("• <b>Wednesday:</b> Breakfast: Aloo Ki Sabji with Puri, Coffee/Tea, Banana. Lunch: Kadai Paneer, Mix Dal, Rice, Chapati, Salad. Tea: Biscuits, Tea. Dinner: Sambhar, Cabbage/Cauliflower, Rice, Chapati, Sweet Dish (Sewaiya).", body_style))
story.append(Paragraph("• <b>Thursday:</b> Breakfast: Onion Mix Paratha, Butter, Dahi, Tea, Fruits. Lunch: Kadhi Pakoda, Aloo-Kala Channa, Rice, Chapati, Salad. Tea: Finger Chips (French Fries) / Mix Pakodi, Coffee. Dinner: Dal Arhar, Baingan Bharta / Pat Gobhi, Rice, Chapati, Sweet Dish (Gulab Jamun).", body_style))
story.append(Paragraph("• <b>Friday:</b> Breakfast: Idli Sambhar with Chutney & Aloo Sandwich (Option B: Kala Chana, Daliya, Apple). Lunch: Chole, Kaddu / Aloo Palak, Rice, Chapati, Dahi. Tea: Macaroni, Bhel Puri, Tea. Dinner: Dal Masoor, Manchurian / Matar Paneer, Fried Rice, Sweet Dish (Fruit Milk Custard).", body_style))
story.append(Paragraph("• <b>Saturday:</b> Breakfast: Palak Paratha / Aloo Paneer Mix Bhurji, Butter, Tea, Banana. Lunch: Dal Malka, Mix Veg, Rice, Chapati, Papad. Tea: Samosa / Aloo Bonda, Tea. Dinner: Rajma / Aloo Matar, Rice, Chapati, Sweet Dish (Suji Halwa).", body_style))
story.append(Paragraph("• <b>Sunday:</b> Breakfast: Chole Bhature, Onion, Pickle, Sunday Tea. Lunch: Special Veg Biryani / Fried Rice, Boondi Raita, Papad. Tea: Biscuits, Tea. Dinner: Chana Dal, Aloo Bharta / Sambhar, Rice, Chapati, Sweet Dish (Ice Cream / White Rasgulla).", body_style))
story.append(Spacer(1, 8))

# 2. Canteen Menu
story.append(Paragraph("2. Campus Canteen Menu & Pricing", h1_style))
story.append(Paragraph("• <b>Burgers:</b> Crispy Veg Burger (Rs. 50), Cheese Lava Burger (Rs. 70), Paneer Supreme Burger (Rs. 80), Aloo Tikki Burger (Rs. 40).", body_style))
story.append(Paragraph("• <b>Momos (Full Plate - 8 Pcs):</b> Veg Steamed Momos (Rs. 60), Veg Fried Momos (Rs. 70), Paneer Steamed Momos (Rs. 80), Paneer Fried Momos (Rs. 90), Kurkure Crunch Momos (Rs. 100).", body_style))
story.append(Paragraph("• <b>Cold Drinks:</b> Coca-Cola 500ml (Rs. 40), Thums Up (Rs. 40), Sprite (Rs. 40), Mountain Dew (Rs. 40), Frooti (Rs. 20), Red Bull (Rs. 125).", body_style))
story.append(Paragraph("• <b>Coffee & Tea:</b> Masala Chai (Rs. 15), Ginger Tea (Rs. 15), Hot Nescafe Coffee (Rs. 25), Black Coffee (Rs. 20).", body_style))
story.append(Paragraph("• <b>Cold Coffee & Shakes:</b> Classic Thick Cold Coffee (Rs. 50), Cold Coffee with Vanilla Ice Cream (Rs. 70), Chocolate Frappe Cold Coffee (Rs. 80), Oreo KitKat Shake (Rs. 90).", body_style))
story.append(Paragraph("• <b>Quick Bites:</b> French Fries (Rs. 60), Peri Peri Fries (Rs. 75), Masala Maggi (Rs. 35), Cheese Maggi (Rs. 55), Grilled Cheese Sandwich (Rs. 60), Paneer Tikka Sandwich (Rs. 75).", body_style))
story.append(Spacer(1, 8))

# 3. Class Timetables
story.append(Paragraph("3. Academic Timetables (1st, 2nd, 3rd, 4th Year)", h1_style))
story.append(Paragraph("• <b>1st Year (B.Tech CSE Sec A):</b> Venue: Block B, Room B-001. Timing: 09:05 - 03:25 PM. Core subjects: Maths-I (Dr. S. K. Iyer), Programming in C (Mr. Gaurav Chaturvedi), Physics (Dr. Atma Rai), Electrical Engg (Mr. Ankit Mainwal), Graphics (Mr. Narendra Bansal), Self Employment Lab (Mr. Abhishek Jain).", body_style))
story.append(Paragraph("• <b>2nd Year (B.Tech CSE Sec IIA-A):</b> Venue: Block C, Room C-202. Timing: 09:05 - 04:15 PM. Core subjects: DSA (Dr. Himanshu Gupta), OOPs Java (Ms. Dimpi Madan), Python (Dr. Deepak Arya), Digital Electronics (Dr. Ranjan Mishra), Discrete Structure (Dr. Akshay Saini), IBM Training (Mr. Adarsh), GFG Competitive Coding (1:45-4:15 PM).", body_style))
story.append(Paragraph("• <b>3rd Year (B.Tech CSE Sec IIIA-A):</b> Venue: Block C, Room C-212. Timing: 09:05 - 05:00 PM. Core subjects: GFG Track (09:05-10:45 AM), Compiler Design (Ms. Bhanupriya), DBMS (Ms. Priti Saini), DAA (Mr. Vipin Jaiswal), Software Engineering (Ms. Chandani), Distributed Systems (Dr. Abhay Bhatia), Constitution of India (Mr. Rao Ragib Khan).", body_style))
story.append(Paragraph("• <b>4th Year (B.Tech Final Year):</b> Venue: Block D, Room D-202. Timing: 09:05 - 04:15 PM. Core subjects: Cloud Computing (Ms. Bhanupriya), Machine Learning (Dr. Gaurav Kumar), Mobile Tech (Ms. Priti Saini), Disaster Management (Dr. Anil Chauhan), Innovations (Ms. Taniya Dhiman), Capstone Project Seminar (Mr. Avnish Chauhan).", body_style))
story.append(Spacer(1, 8))

# 4. Academic Regulations
story.append(Paragraph("4. Academic Regulations & Attendance Policy", h1_style))
story.append(Paragraph("• <b>Mandatory Attendance Rule:</b> Minimum <b>75%</b> attendance is required in each theory and laboratory course.", body_style))
story.append(Paragraph("• <b>Medical Condonation:</b> Up to 10% condonation (minimum 65%) on valid medical grounds with CMO medical certificate.", body_style))
story.append(Paragraph("• <b>Detention:</b> Attendance below 65% results in strict detention from appearing in End-Semester examinations.", body_style))
story.append(Paragraph("• <b>Evaluation:</b> 40% Internal Assessment + 60% End-Semester Examination.", body_style))

doc.build(story)
print(f"Successfully generated updated RIT handbook: {output_pdf}")
