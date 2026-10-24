# 🎓 CampusMitra AI — Autonomous Indian Campus Concierge
### Fetch.ai / ASI:One Agent Challenge (Fetch-A-Thon 3.0) — *From Intent to Action*

[![Fetch.ai](https://img.shields.io/badge/Fetch.ai-uAgents_v0.26-blue.svg)](https://fetch.ai/)
[![Agentverse](https://img.shields.io/badge/Agentverse-Registered_%26_Active-success.svg)](https://agentverse.ai/)
[![ASI:One](https://img.shields.io/badge/ASI:One-Interactive_Cards_v1-indigo.svg)](https://asi1.ai/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/Frontend-React_+_Tailwind_CSS-38bdf8.svg)](https://react.dev/)
[![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB_RAG-orange.svg)](https://www.trychroma.com/)

---

## 🌟 Executive Summary

**CampusMitra AI** is a multi-agent, campus-level AI assistant tailored specifically for Indian university and engineering institute ecosystems. Built natively on **Fetch.ai's Agent Chat Protocol (ACP)** and the **ASI:One Interactive Cards Protocol**, CampusMitra AI enables students, professors, and visitors to navigate campus life seamlessly inside ASI:One or via a modern React + Tailwind web dashboard.

---

## 🏗️ Architecture & Technology Stack

| Component | Technology | Implementation Details |
| :--- | :--- | :--- |
| **Frontend** | **React + Tailwind CSS** | Interactive campus portal with timetable viewer, building floor maps, faculty cabin search, and full ASI card rendering. |
| **Backend** | **Python + FastAPI** | High-performance asynchronous REST API (`/api/chat`, `/api/timetables`, `/api/buildings`, `/api/faculty`, `/api/rag/query`). |
| **AI Model & Agents** | **Multi-Agent Orchestrator** | Specialized agents: `TimetableAgent`, `NavigationAgent`, `FacultyAgent`, and `RAGAgent`. |
| **College Documents** | **RAG Pipeline (`pypdf`)** | Ingests official PDF Academic Handbook, extracts rules, and builds chunked semantic contexts. |
| **Vector Database** | **ChromaDB** | Persistent vector store (`chroma_db/`) indexing academic regulations, attendance rules, and fee policies. |
| **Agent Framework** | **Fetch.ai `uagents` (v0.26.1)** | Implements `AgentChatProtocol:0.3.0` with `ChatMessage` and `ChatAcknowledgement`. |
| **Interactive Cards** | **ASI Cards Protocol v1** | Generates `carousel`, `detail`, `form`, and `review` cards for zero-typing UI interaction. |

---

## 🏛️ Campus Knowledge Base Details

### 1. Campus Buildings & Classroom Floor Maps
- **Alan Turing Computer Science Block (`CS-BLOCK`)**: 4 Floors. Houses 1st Year (CS-101/102), 2nd Year CSE (CS-201/202), 3rd Year CSE (CS-301/302), and 4th Year CSE (CS-401/402). 1st Floor has the HOD Office and Cloud Systems Lab. 2nd Floor features the AI & Machine Learning Research Center with NVIDIA RTX 4090 GPUs. 3rd Floor houses the IoT Hardware Lab and Departmental Auditorium.
- **Ramanujan Academic Block (`AB-MAIN`)**: 3 Floors. Ground Floor holds Lecture Theaters LT-1 and LT-2, the Student Section, and Accounts Office. 1st Floor holds Room 201, Room 202, and Physics Laboratory. 2nd Floor hosts Applied Mathematics Hall and the Dean of Academics Office.
- **Vikram Sarabhai Electronics Block (`ECE-BLOCK`)**: 3 Floors. Ground Floor contains EC-101 and Analog/DSP Labs. 1st Floor features EC-201, EC-202, and the VLSI Semiconductor Design Lab. 2nd Floor contains EC-301, EC-401, and the Microwave & Antenna Lab.
- **Central Knowledge & Library Complex (`CENTRAL-LIB`)**: 2 Floors. Ground Floor handles Circulation and General Stacks. 1st Floor features the 24/7 Air-Conditioned Silent Reading Hall (220 seats), Digital Research Lab (IEEE/Springer access), and Group Discussion Rooms A & B.

### 2. Timetables (All 4 Years, Monday - Friday)
- **1st Year (B.Tech Foundation)**: Venue: *Ramanujan LT-1*. Engineering Maths-I, Applied Physics, C Programming, Electrical Engineering, Labs.
- **2nd Year (CSE Core)**: Venue: *Turing CS-201*. Data Structures & Algorithms, Discrete Maths, Java OOPs, Digital Logic, Simulation Labs.
- **3rd Year (CSE Junior)**: Venue: *Turing CS-301*. Operating Systems, DBMS, Machine Learning, Computer Networks, Linux Kernel Lab.
- **4th Year (CSE Specialization)**: Venue: *Turing CS-401*. Distributed Systems & Cloud, Deep Learning & Generative AI, Cybersecurity, Major Project Defense.

### 3. Faculty Directory & Cabin Locations
- **Dr. Rajesh Sharma (HOD)**: Computer Science · Subjects: Data Structures & Algorithms · Cabin: *Turing 1st Floor, CS-105* · Visiting: *Mon & Wed, 2:00 PM - 4:00 PM*.
- **Prof. Ananya Verma**: Computer Science · Subjects: Operating Systems, OOPs Java · Cabin: *Turing 2nd Floor, CS-204* · Visiting: *Tue & Thu, 11:00 AM - 1:00 PM*.
- **Dr. Amit Gupta**: Computer Science · Subjects: DBMS, Cloud Computing · Cabin: *Turing 2nd Floor, CS-210* · Visiting: *Mon & Fri, 3:00 PM - 5:00 PM*.
- **Prof. Neha Kapoor**: AI & Data Science · Subjects: Machine Learning, Deep Learning · Cabin: *Turing 3rd Floor, CS-308* · Visiting: *Wed & Thu, 1:30 PM - 3:30 PM*.
- **Dr. S. K. Iyer**: Mathematics · Subjects: Engg Mathematics, Discrete Maths · Cabin: *Ramanujan 2nd Floor, RM-201* · Visiting: *Mon, Tue, Fri, 12:00 PM - 1:00 PM*.
- **Dr. P. V. Reddy**: Electronics & Comm · Subjects: Basic Electronics, Digital Logic, DSP · Cabin: *Sarabhai 1st Floor, EC-108* · Visiting: *Tue & Thu, 2:00 PM - 4:00 PM*.

---

## 🌐 Agentverse Live Registration

CampusMitra AI is **registered and active** on Agentverse:
- **Agent Name**: `CampusMitra AI`
- **Agent Address**: `agent1qt6msz8tyzg629x2uhvjn025sd27erneyl4427fpgdxqq74ycryquewctvc`
- **Agentverse Profile URL**: [https://agentverse.ai/agents/agent1qt6msz8tyzg629x2uhvjn025sd27erneyl4427fpgdxqq74ycryquewctvc](https://agentverse.ai/agents/agent1qt6msz8tyzg629x2uhvjn025sd27erneyl4427fpgdxqq74ycryquewctvc)
- **ASI:One URL**: [https://asi1.ai/](https://asi1.ai/)

---

## 🚀 Quickstart Guide

### 1. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. Configure Environment (`.env`)
```ini
AGENTVERSE_API_KEY=your_agentverse_api_key_here
CAMPUS_AGENT_SEED=campus mitra indian college concierge pilot seed 2026
FASTAPI_PORT=8080
UAGENT_PORT=8000
```

### 3. Run the Complete System
```bash
python run_campus.py
```
This starts:
1. **FastAPI Web & REST Server**: `http://127.0.0.1:8080/`
2. **Fetch.ai uAgent ACP Service**: `http://127.0.0.1:8000/submit`

### 4. 24/7 Cloud Deployment on Agentverse
To host CampusMitra AI in the cloud with zero local server requirements:
1. Open [Agentverse](https://agentverse.ai/) and log in.
2. Click **"+ New Agent"** -> Choose **"Blank Agent"**.
3. Open `campus_mitra/hosted_agent.py`, copy all its contents, and paste into the Agentverse Code Editor.
4. Click **"Run"** -> CampusMitra AI is live 24/7 on Agentverse and ready in ASI:One!

---

## 🧪 Automated Testing

Run the end-to-end ACP client test:
```bash
python test_campus_client.py
```
This tests:
1. Main Menu Carousel Card
2. Timetable Detail Card (3rd Year Wednesday)
3. Room & Lab Location Search (CS-201)
4. Faculty Cabin & Visiting Hours Card (Dr. Rajesh Sharma)
5. Academic Handbook RAG Search (75% Attendance & Condonation)
