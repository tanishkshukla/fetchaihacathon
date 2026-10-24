"""
YieldSentinel - Register Worker Agent (DeFi Risk Analyst) on Agentverse
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
RISK_AGENT_SEED = os.getenv("RISK_AGENT_SEED", "defi-risk-analyst-agent-seed-secure-beta")

identity = Identity.from_seed(RISK_AGENT_SEED, 0)
print(f"[*] Registering Worker Agent: DeFi Risk Analyst")
print(f"[*] Address: {identity.address}")

credentials = RegistrationRequestCredentials(
    agent_seed_phrase=RISK_AGENT_SEED,
    agentverse_api_key=AGENTVERSE_API_KEY,
)

readme_content = """# DeFi Risk Analyst AI — Security & Audit Verification Worker

Specialized worker agent operating in collaboration with YieldSentinel AI.

## Responsibilities
- Verifies protocol TVL liquidity thresholds.
- Cross-references multi-firm security audits (CertiK, Halborn, PeckShield, OpenZeppelin).
- Evaluates slashing mitigation parameters.
- Issues cryptographic security validation certificates for staking allocations.
"""

try:
    success = register_chat_agent(
        name="DeFi Risk Analyst",
        endpoint="https://agentverse.ai/v1/proxy",
        active=True,
        credentials=credentials,
        description="Specialized worker agent verifying smart contract audits, slashing safeguards, and liquidity metrics.",
        readme=readme_content,
        avatar_url="https://assets.coingecko.com/coins/images/16724/standard/osmo.png",
        metadata={
            "categories": ["defi", "risk-management", "security", "auditing"],
            "is_public": "True",
        }
    )
    print(f"\n[SUCCESS] Risk Analyst registered on Agentverse! Status: {success}")
    print(f"[PROFILE] View at: https://agentverse.ai/agents/{identity.address}")
except Exception as e:
    print(f"\n[ERROR] Registration failed: {e}")
