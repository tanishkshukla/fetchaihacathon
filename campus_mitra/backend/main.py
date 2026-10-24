"""
CampusMitra AI - FastAPI Backend Service
Provides RESTful APIs for the React + Tailwind frontend, RAG retrieval,
campus directory, timetables, and multi-agent conversational routing.
"""
import os
import sys
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv

# Ensure root and campus_mitra are in python path
current_dir = os.path.dirname(os.path.abspath(__file__))
mitra_dir = os.path.abspath(os.path.join(current_dir, ".."))
workspace_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
for p in [mitra_dir, workspace_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

load_dotenv(os.path.join(mitra_dir, ".env"))

from backend.data.campus_data import (
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
    get_all_buildings,
    get_all_faculty,
)
from backend.rag.vector_store import get_vector_store
from backend.agents.orchestrator import CampusMitraOrchestrator

app = FastAPI(
    title="CampusMitra AI API",
    description="Intelligent Indian Campus Concierge with RAG, Timetables, and ASI Interactive Cards",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Orchestrator & Vector Store
orchestrator = CampusMitraOrchestrator()
vector_store = get_vector_store()


# Request / Response Schemas
class ChatRequest(BaseModel):
    message: str
    session: Optional[Dict[str, Any]] = None


class RAGQueryRequest(BaseModel):
    query: str
    top_k: Optional[int] = 3


# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------
@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "CampusMitra AI Backend",
        "chromadb_chunks": vector_store.collection.count() if vector_store.collection else len(vector_store.fallback_chunks),
        "buildings_count": len(BUILDINGS),
        "faculty_count": len(FACULTY_MEMBERS),
        "timetables_available": list(TIMETABLES.keys())
    }


@app.post("/api/chat")
def chat_endpoint(req: ChatRequest):
    session = req.session or {}
    response = orchestrator.process_request(req.message, session)
    return response


@app.get("/api/timetables")
def list_timetables():
    return {
        "years": {k: {"title": v["title"], "classroom": v["classroom"]} for k, v in TIMETABLES.items()}
    }


@app.get("/api/timetables/{year_key}/{day}")
def get_specific_timetable(year_key: str, day: str):
    if year_key not in TIMETABLES:
        raise HTTPException(status_code=404, detail="Academic year not found")
    return get_timetable(year_key, day)


@app.get("/api/buildings")
def list_buildings():
    return get_all_buildings()


@app.get("/api/buildings/{bldg_id}")
def get_building(bldg_id: str):
    b = get_building_by_id(bldg_id)
    if not b:
        raise HTTPException(status_code=404, detail="Building not found")
    return b


@app.get("/api/rooms/search")
def search_rooms(q: str):
    return find_room_location(q)


@app.get("/api/faculty")
def list_faculty():
    return get_all_faculty()


@app.get("/api/faculty/{fac_id}")
def get_faculty(fac_id: str):
    f = get_faculty_by_id(fac_id)
    if not f:
        raise HTTPException(status_code=404, detail="Faculty member not found")
    return f


@app.get("/api/mess")
def get_mess(day: Optional[str] = None):
    if day:
        return get_mess_menu(day)
    return {
        "timings": MESS_TIMINGS,
        "weekly_menu": MESS_MENU
    }


@app.get("/api/canteen")
def get_canteen():
    return get_canteen_menu()


@app.post("/api/rag/query")
def rag_search(req: RAGQueryRequest):
    hits = vector_store.search(req.query, n_results=req.top_k)
    return {
        "query": req.query,
        "hits_count": len(hits),
        "hits": hits
    }


@app.get("/api/agentverse/status")
def agentverse_status():
    api_key_present = bool(os.getenv("AGENTVERSE_API_KEY"))
    return {
        "platform": "Fetch.ai Agentverse",
        "api_key_configured": api_key_present,
        "agent_name": "campus_mitra_ai",
        "protocol": "AgentChatProtocol:0.3.0",
        "card_protocol_version": "1",
        "supported_card_kinds": ["carousel", "detail", "form", "review"]
    }


# ---------------------------------------------------------------------------
# Frontend Root Route: Serves the React + Tailwind UI
# ---------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def serve_ui():
    html_file = os.path.join(mitra_dir, "frontend", "index.html")
    if os.path.exists(html_file):
        with open(html_file, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>CampusMitra AI Backend is running. Frontend index.html not found.</h1>"


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("FASTAPI_PORT", 8080))
    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=False)
