"""
YieldSentinel - Multi-Agent Bureau Runner
Starts both YieldSentinel (Orchestrator ACP agent) and Risk Analyst (Worker agent).
"""

import asyncio
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from uagents import Bureau
from src.sentinel_agent import agent as sentinel_agent
from src.risk_agent import risk_agent

# Initialize Bureau to manage multi-agent lifecycle
bureau = Bureau(port=8000)
bureau.add(sentinel_agent)
bureau.add(risk_agent)

if __name__ == "__main__":
    print("================================================================")
    print("[*] Starting YieldSentinel AI Multi-Agent System")
    print("   1. Sentinel Agent (ASI:One ACP + Interactive Cards)")
    print("   2. Risk Analyst Agent (DeFi Audits & Safety Verification)")
    print("================================================================")
    bureau.run()
