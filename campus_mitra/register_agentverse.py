"""
CampusMitra AI - Agentverse Registration Script
Registers / Updates the CampusMitra AI agent on Agentverse (https://agentverse.ai/)
using the provided AGENTVERSE_API_KEY.
"""
import os
import sys
from dotenv import load_dotenv

mitra_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(mitra_dir, ".env"))

from uagents.crypto import Identity
from uagents_core.utils.registration import (
    RegistrationRequestCredentials,
    register_chat_agent,
    AgentverseRequestError,
)

AGENTVERSE_API_KEY = os.getenv("AGENTVERSE_API_KEY")
CAMPUS_AGENT_SEED = os.getenv("CAMPUS_AGENT_SEED", "campus mitra indian college concierge pilot seed 2026")

if not AGENTVERSE_API_KEY:
    print("[ERROR] AGENTVERSE_API_KEY is not set in .env file!")
    sys.exit(1)

# Derive identity
identity = Identity.from_seed(CAMPUS_AGENT_SEED, 0)
print(f"[*] Updating Agent on Agentverse: CampusMitra AI")
print(f"[*] Address: {identity.address}")

credentials = RegistrationRequestCredentials(
    agent_seed_phrase=CAMPUS_AGENT_SEED,
    agentverse_api_key=AGENTVERSE_API_KEY,
)

readme_content = """# CampusMitra AI — Smart Indian Campus Concierge (RIT Edition)

CampusMitra AI is an autonomous, campus-level AI assistant built on Fetch.ai / ASI:One protocol for Indian universities and engineering institutes.

## Key Capabilities
- **Official Class Timetables (All 4 Years)**: Complete Monday-Saturday routines for 1st Year (Room B-001), 2nd Year (Room C-202), 3rd Year (Room C-212), and 4th Year (Room D-202).
- **Boys Hostel Mess Menu (Mon - Sun)**: Breakfast (07:30 AM), Lunch (12:45 PM), Evening Tea/Snacks (05:15 PM), and Dinner (08:00 PM) with weekly sweet dishes (Kheer, Jalebi, Gulab Jamun, Ice Cream).
- **Campus Canteen Menu**: Burgers, Full Plate Momos, Cold Drinks (Coke, Thums Up, Sprite), Hot Coffee, Kadak Chai, Thick Cold Coffee, and Snacks with student pricing.
- **Campus Buildings & Floor Maps**: Academic Block B, Block C, Block D, and Central Amenities Complex.
- **Faculty Directory & Cabins**: Professor profiles, subjects taught, cabin numbers, and office visiting hours.
- **Academic Handbook RAG**: Semantic vector retrieval powered by ChromaDB indexing the official PDF handbook for 75% attendance rules, medical condonation, evaluation criteria, and fee deadlines.
- **ASI Interactive Cards Protocol**: Uses Carousel, Detail, Form, and Review cards for zero-friction interaction in ASI:One.

## How to Interact in ASI:One
- Ask: *"What is in Sunday breakfast mess?"*
- Ask: *"Show campus canteen burger and momos menu"*
- Ask: *"Show 4th year timetable for Friday"*
- Ask: *"Where is room C-202 located?"*
- Ask: *"Where is Dr. Lokesh Kumar's cabin?"*
- Browse interactive carousel cards and select days or meals directly!
"""

try:
    success = register_chat_agent(
        name="CampusMitra AI",
        endpoint="http://localhost:8000/submit",
        active=True,
        credentials=credentials,
        description="Indian Campus AI Concierge: 1st-4th year timetables, hostel mess food, canteen menu, classrooms, and handbook RAG.",
        readme=readme_content,
        avatar_url="https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=200",
        starter_prompts=[
            "What is in Sunday breakfast mess?",
            "Show campus canteen burger and momos menu",
            "Show 4th year timetable for Friday",
            "Show 2nd year CSE timetable for Wednesday",
            "Where is room C-202 located?"
        ],
        metadata={
            "categories": ["education", "campus", "assistant", "productivity", "food", "rag"],
            "is_public": "True",
        }
    )
    print(f"\n[SUCCESS] CampusMitra AI updated on Agentverse! Status: {success}")
    print(f"[PROFILE] View your agent at: https://agentverse.ai/agents/{identity.address}")
    print(f"[ASI:ONE] Interact with CampusMitra in ASI:One at: https://asi1.ai/")
except AgentverseRequestError as e:
    print(f"\n[ERROR] Registration failed: {e}")
except Exception as e:
    print(f"\n[UNEXPECTED ERROR] {e}")
