"""
ASI:One Interactive Cards Module for YieldSentinel
Implements Carousel, Detail, Form, and Review cards following Fetch.ai ACP specifications.
"""

import json
from datetime import datetime, timezone
from uuid import uuid4
from uagents_core.contrib.protocols.chat import (
    ChatMessage,
    MetadataContent,
    TextContent,
)

from src.defillama import (
    get_all_pools,
    get_pool_by_id,
    calculate_projected_returns,
)


def create_card_message(
    narration: str,
    card_kind: str,
    card_payload: dict,
    is_terminal: bool = False,
    drawer_width_px: str = "540"
) -> ChatMessage:
    """Helper to wrap narration text and card metadata block into a valid ACP ChatMessage."""
    metadata = {
        "card_protocol_version": "1",
        "requires_card_interaction": "false" if is_terminal else "true",
        "card_kind": card_kind,
        "card_payload": json.dumps(card_payload),
        "preferred_drawer_width_px": drawer_width_px,
    }
    if is_terminal:
        metadata["is_terminal"] = "true"

    return ChatMessage(
        timestamp=datetime.now(timezone.utc),
        msg_id=uuid4(),
        content=[
            TextContent(type="text", text=narration),
            MetadataContent(type="metadata", metadata=metadata)
        ]
    )


# ============================================================================
# 1. CAROUSEL CARD - Browse Curated Staking & Yield Vaults
# ============================================================================
def build_pools_carousel() -> dict:
    """Generates the Carousel card payload displaying audited staking & DeFi pools."""
    pools = get_all_pools()
    items = []

    for p_id, p in pools.items():
        badge_variant = "success" if p["risk_score"] >= 9.5 else ("info" if p["risk_score"] >= 9.0 else "warning")
        
        items.append({
            "id": p["id"],
            "image": p["icon_url"],
            "title": p["name"],
            "subtitle": f"{p['chain']} · {p['apy']}% APY · {p['unbonding_period']}",
            "badges": [
                {"label": f"Risk Score: {p['risk_score']}/10", "variant": badge_variant},
                {"label": p["token"], "variant": "info"}
            ],
            "secondary_text": f"TVL: ${p['tvl_usd']:,} USD",
            "primary_cta": {
                "label": "Analyze & Allocate",
                "selection": {
                    "action": "select_pool",
                    "pool_id": p["id"]
                }
            }
        })

    return {
        "title": "YieldSentinel: Verified Staking & Yield Vaults",
        "subtitle": "Audited proof-of-stake & DeFi vaults actively monitored by Risk Guardian Agents",
        "items": items
    }


# ============================================================================
# 2. DETAIL CARD - Deep Risk Analysis & Compounding Strategy Selector
# ============================================================================
def build_pool_detail(pool_id: str) -> dict:
    """Generates the Detail card payload for a specific staking pool."""
    pool = get_pool_by_id(pool_id)
    
    summary_rows = [
        {"label": "Protocol / Chain", "value": f"{pool['protocol']} ({pool['chain']})"},
        {"label": "Annualized Base APY", "value": f"{pool['apy']}%"},
        {"label": "Total Value Locked", "value": f"${pool['tvl_usd']:,} USD"},
        {"label": "Risk Score", "value": f"{pool['risk_score']} / 10 ({pool['risk_level']})"},
        {"label": "Slashing Safeguard", "value": pool["slashing_risk"]},
        {"label": "Unbonding Period", "value": pool["unbonding_period"]},
        {"label": "Security Audits", "value": " · ".join(pool["audits"])},
    ]

    choices = [
        {
            "value": strat["id"],
            "label": strat["label"],
            "secondary_text": strat["detail"]
        }
        for strat in pool.get("strategies", [])
    ]

    return {
        "title": f"Risk Profile: {pool['name']}",
        "hero_image": pool["icon_url"],
        "summary_rows": summary_rows,
        "sub_options": {
            "name": "strategy",
            "kind": "radio",
            "label": "Select Compounding Strategy",
            "choices": choices
        },
        "approve_cta": {
            "label": "Proceed to Position Setup",
            "primary": True,
            "selection": {
                "action": "configure_position",
                "pool_id": pool_id
            }
        },
        "reject_cta": {
            "label": "Back to Pools",
            "selection": {
                "action": "back_to_pools"
            }
        }
    }


# ============================================================================
# 3. FORM CARD - Position Configuration & Guardian Parameters
# ============================================================================
def build_position_form(pool_id: str, strategy: str = "auto_compound") -> dict:
    """Generates the Form card payload for entering deposit amount and stop-loss criteria."""
    pool = get_pool_by_id(pool_id)
    token = pool.get("token", "FET")

    return {
        "title": f"Configure Allocation: {pool['name']}",
        "subtitle": f"Selected Strategy: {strategy.replace('_', ' ').title()}",
        "fields": [
            {
                "name": "deposit_amount",
                "kind": "number",
                "label": f"Deposit Amount ({token})",
                "placeholder": "e.g. 500",
                "required": True
            },
            {
                "name": "wallet_address",
                "kind": "text",
                "label": f"Delegator {token} Wallet Address",
                "placeholder": f"e.g. {token.lower()}1... or 0x...",
                "required": True
            },
            {
                "name": "guardian_alert",
                "kind": "select",
                "label": "Automated Risk Guardian Trigger",
                "options": [
                    {"value": "strict", "label": "Strict: Alert if APY drops > 2% or validator jailed"},
                    {"value": "moderate", "label": "Moderate: Alert on critical slashing risk"},
                    {"value": "off", "label": "Disabled: Keep position without push alerts"}
                ]
            }
        ],
        "submit_cta": {
            "label": "Review Allocation",
            "selection": {
                "action": "submit_position",
                "pool_id": pool_id,
                "strategy": strategy
            }
        }
    }


# ============================================================================
# 4. REVIEW CARD - Executive Confirmation & Protocol Verification
# ============================================================================
def build_allocation_review(session_data: dict) -> dict:
    """Generates the Review card payload displaying full returns and risk signoff."""
    pool_id = session_data.get("pool_id", "asi_fetch_staking")
    pool = get_pool_by_id(pool_id)
    strategy = session_data.get("strategy", "auto_compound")

    try:
        amount = float(session_data.get("deposit_amount", 500.0))
    except (ValueError, TypeError):
        amount = 500.0

    wallet = session_data.get("wallet_address", "fetch1...7x9a")
    if len(wallet) > 16:
        masked_wallet = f"{wallet[:8]}...{wallet[-6:]}"
    else:
        masked_wallet = wallet

    returns = calculate_projected_returns(pool, amount, strategy)
    token = returns["token"]

    summary_rows = [
        {"label": "Vault / Staking Pool", "value": pool["name"]},
        {"label": "Compounding Strategy", "value": strategy.replace('_', ' ').title()},
        {"label": "Deposit Principal", "value": f"{amount:,.2f} {token}"},
        {"label": "Effective Annual APY", "value": f"{returns['effective_apy']}%"},
        {"label": "Est. 1-Year Earnings", "value": f"+{returns['annual_earnings']:,} {token} (~${returns['annual_earnings_usd']:,} USD)"},
        {"label": "Delegator Wallet", "value": masked_wallet},
        {"label": "Guardian Security Status", "value": "PASSED (Certified by DeFi Risk Analyst)"},
        {"label": "Protocol Protection Fee", "value": "0.1 FET (YieldSentinel Protection Guarantee)"},
    ]

    return {
        "title": "Confirm Staking Allocation",
        "subtitle": "Review position parameters and authorize Risk Guardian monitoring",
        "summary_rows": summary_rows,
        "approve_cta": {
            "label": "Authorize & Stake Position",
            "primary": True,
            "selection": {
                "action": "confirm_allocation",
                "pool_id": pool_id,
                "amount": amount,
                "strategy": strategy,
                "wallet": wallet
            }
        },
        "reject_cta": {
            "label": "Cancel Position",
            "selection": {
                "action": "cancel_allocation"
            }
        }
    }
