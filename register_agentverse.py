"""
YieldSentinel - Automatic Agentverse Registration Script
Registers the YieldSentinel agent profile, ACP chat protocol digest,
avatar, description, and starter prompts on Agentverse.
"""

import os
from dotenv import load_dotenv
from uagents.crypto import Identity
from uagents_core.utils.registration import (
    RegistrationRequestCredentials,
    register_chat_agent,
    AgentverseRequestError,
)

load_dotenv()

AGENTVERSE_API_KEY = os.getenv("AGENTVERSE_API_KEY")
SENTINEL_AGENT_SEED = os.getenv("SENTINEL_AGENT_SEED", "yield-sentinel-asi-hackathon-2026-seed-alpha")

if not AGENTVERSE_API_KEY:
    print("[ERROR] AGENTVERSE_API_KEY is not set in .env file!")
    exit(1)

# Derive identity from seed phrase
identity = Identity.from_seed(SENTINEL_AGENT_SEED, 0)
print(f"[*] Registering Agent: YieldSentinel AI")
print(f"[*] Address: {identity.address}")

credentials = RegistrationRequestCredentials(
    agent_seed_phrase=SENTINEL_AGENT_SEED,
    agentverse_api_key=AGENTVERSE_API_KEY,
)

readme_content = """# YieldSentinel AI — Autonomous DeFi & Staking Risk Guardian

YieldSentinel AI is an autonomous, agentic risk guardian built for the Fetch.ai / ASI Alliance ecosystem and cross-chain DeFi.

## Core Capabilities
- **Curated Yield Vaults**: Real-time tracking of top staking and DeFi pools (Fetch.ai Native, Osmosis, Aave, Lido).
- **Interactive UI Drawers**: Driven entirely inside ASI:One using Interactive Cards (Carousel, Detail, Form, Review).
- **Automated Risk Assessment**: Secondary worker agent validates protocol TVL, security audits (CertiK, OpenZeppelin), and slashing safeguards.
- **Verifiable Allocations**: Generates on-chain allocation records and continuous 24/7 slashing/APY anomaly monitoring.

## How to Interact in ASI:One
1. Ask: *"Find high yield staking with low risk"* or *"Show me staking vaults"*.
2. Browse the **Carousel Card** of audited vaults.
3. Inspect security metrics on the **Detail Card** and pick your compounding strategy.
4. Fill the **Form Card** with your deposit amount and wallet.
5. Review projected 1-year earnings and confirm your allocation on the **Review Card**.
"""

try:
    success = register_chat_agent(
        name="YieldSentinel AI",
        endpoint="http://localhost:8000/submit",
        active=True,
        credentials=credentials,
        description="Autonomous DeFi & Staking Risk Guardian with interactive cards for yield optimization and validator monitoring.",
        readme=readme_content,
        avatar_url="https://assets.coingecko.com/coins/images/5681/standard/Fetch.jpg",
        starter_prompts=[
            "Find the best staking yields for FET and stablecoins",
            "Show me audited staking vaults",
            "What is the current APY for Fetch.ai native staking?",
            "Analyze DeFi yields and risk scores"
        ],
        metadata={
            "categories": ["defi", "finance", "staking", "yield-farming", "risk-management"],
            "is_public": "True",
        }
    )
    print(f"\n[SUCCESS] Agent registered on Agentverse! Status: {success}")
    print(f"[PROFILE] View your agent at: https://agentverse.ai/agents/{identity.address}")
    print(f"[ASI:ONE] Test in ASI:One at: https://asi1.ai/")
except AgentverseRequestError as e:
    print(f"\n[ERROR] Registration failed: {e}")
except Exception as e:
    print(f"\n[UNEXPECTED ERROR] {e}")
