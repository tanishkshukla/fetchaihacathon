import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Agentverse API
AGENTVERSE_API_KEY = os.getenv("AGENTVERSE_API_KEY", "")

# Seeds for deterministic agent addresses
SENTINEL_AGENT_SEED = os.getenv("SENTINEL_AGENT_SEED", "yield-sentinel-asi-hackathon-2026-seed-alpha")
RISK_AGENT_SEED = os.getenv("RISK_AGENT_SEED", "defi-risk-analyst-agent-seed-secure-beta")

# Agent Names & Metadata
SENTINEL_AGENT_NAME = "yield_sentinel"
RISK_AGENT_NAME = "risk_analyst"

# Local Ports (when running with endpoint)
AGENT_PORT = int(os.getenv("AGENT_PORT", "8000"))
RISK_AGENT_PORT = int(os.getenv("RISK_AGENT_PORT", "8001"))
