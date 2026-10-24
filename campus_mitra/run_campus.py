"""
CampusMitra AI - Master System Runner
Spins up both the FastAPI Web & REST Server (Port 8080)
and the Fetch.ai uAgent with ACP protocol (Port 8000).
"""
import os
import sys
import subprocess
import time
import signal

python_exe = sys.executable
current_dir = os.path.dirname(os.path.abspath(__file__))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=" * 70)
print("  CAMPUSMITRA AI - INDIAN CAMPUS CONCIERGE")
print("  React + Tailwind CSS | FastAPI | ChromaDB RAG | Fetch.ai uAgents")
print("=" * 70)

# Check Agentverse Registration
print("[*] Agentverse Address: agent1qt6msz8tyzg629x2uhvjn025sd27erneyl4427fpgdxqq74ycryquewctvc")
print("[*] Web Dashboard: http://127.0.0.1:8080/")
print("[*] uAgent ACP Endpoint: http://127.0.0.1:8000/submit")
print("-" * 70)

# Start FastAPI in background process
fastapi_cmd = [
    python_exe, "-m", "uvicorn", "backend.main:app",
    "--host", "127.0.0.1",
    "--port", "8080",
    "--app-dir", current_dir
]

uagent_cmd = [
    python_exe, os.path.join(current_dir, "backend", "uagent_service.py")
]

processes = []

try:
    print("[1/2] Starting FastAPI Backend & React Dashboard on http://127.0.0.1:8080...")
    p_fastapi = subprocess.Popen(fastapi_cmd, cwd=current_dir)
    processes.append(p_fastapi)
    time.sleep(2)

    print("[2/2] Starting Fetch.ai uAgent ACP Service on port 8000...")
    p_uagent = subprocess.Popen(uagent_cmd, cwd=current_dir)
    processes.append(p_uagent)

    print("\n[ONLINE] Both services are running successfully!")
    print("Press Ctrl+C to terminate both services.\n")

    # Monitor processes
    while True:
        for p in processes:
            ret = p.poll()
            if ret is not None:
                print(f"[EXIT] Process {p.args} exited with code {ret}")
                sys.exit(ret)
        time.sleep(1)

except KeyboardInterrupt:
    print("\n[*] Shutting down CampusMitra AI...")
    for p in processes:
        p.terminate()
    print("[*] All processes terminated cleanly.")
