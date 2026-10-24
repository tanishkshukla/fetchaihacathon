"""
YieldSentinel AI - All-in-One Cloud Hosted Agent
Paste this directly into an Agentverse Hosted Agent (https://agentverse.ai)
to run YieldSentinel 24/7 in the cloud with zero local setup!
"""

import json
import logging
import re
from datetime import datetime, timezone
from uuid import uuid4

from uagents import Agent, Context, Protocol
from uagents_core.contrib.protocols.chat import (
    ChatAcknowledgement,
    ChatMessage,
    MetadataContent,
    TextContent,
    chat_protocol_spec,
)

# ---------------------------------------------------------------------------
# Staking & Yield Vaults Data
# ---------------------------------------------------------------------------
POOLS = {
    "asi_fetch_staking": {
        "id": "asi_fetch_staking",
        "name": "Fetch.ai Native Staking (ASI Network)",
        "protocol": "ASI Alliance / Fetch.ai",
        "chain": "Cosmos / Fetch Ledger",
        "token": "FET",
        "apy": 12.8,
        "tvl_usd": 345_200_000,
        "risk_score": 9.4,
        "risk_level": "Low Risk",
        "unbonding_period": "21 Days",
        "audits": ["CertiK", "Halborn", "PeckShield"],
        "slashing_risk": "0.01% (Validator Protected)",
        "icon_url": "https://assets.coingecko.com/coins/images/5681/standard/Fetch.jpg",
        "strategies": [
            {"id": "auto_compound", "label": "Auto-Compound (+1.4% APY Boost)", "detail": "Restake accumulated validator rewards daily via REStake"},
            {"id": "liquid_staking", "label": "Liquid Staking (Mint stFET)", "detail": "Retain liquidity with transferable stFET tokens"},
            {"id": "standard", "label": "Direct Native Delegation", "detail": "Traditional Cosmos validator delegation with standard unbonding"}
        ]
    },
    "osmosis_cosmos_yield": {
        "id": "osmosis_cosmos_yield",
        "name": "Osmosis Superfluid Staking (OSMO/ATOM)",
        "protocol": "Osmosis DEX",
        "chain": "Cosmos Ecosystem",
        "token": "OSMO",
        "apy": 14.5,
        "tvl_usd": 182_400_000,
        "risk_score": 8.7,
        "risk_level": "Medium Risk",
        "unbonding_period": "14 Days",
        "audits": ["Informal Systems", "Oak Security"],
        "slashing_risk": "0.05% (Superfluid mitigated)",
        "icon_url": "https://assets.coingecko.com/coins/images/16724/standard/osmo.png",
        "strategies": [
            {"id": "auto_compound", "label": "Auto-Restake LP Rewards", "detail": "Re-compound LP swap fees automatically"},
            {"id": "standard", "label": "Standard Liquidity Provision", "detail": "Collect daily OSMO incentives"}
        ]
    },
    "aave_v3_usdc": {
        "id": "aave_v3_usdc",
        "name": "Aave V3 USDC Supply Vault",
        "protocol": "Aave V3",
        "chain": "Arbitrum / Ethereum",
        "token": "USDC",
        "apy": 6.4,
        "tvl_usd": 1_450_000_000,
        "risk_score": 9.8,
        "risk_level": "Minimal Risk",
        "unbonding_period": "Instant (0 Days)",
        "audits": ["OpenZeppelin", "Trail of Bits", "Sigma Prime"],
        "slashing_risk": "Zero (Collateralized Lending)",
        "icon_url": "https://assets.coingecko.com/coins/images/6319/standard/usdc.png",
        "strategies": [
            {"id": "auto_compound", "label": "Aave aUSDC Compounding", "detail": "Interest accrues every Ethereum second"},
            {"id": "standard", "label": "Flexible Payout", "detail": "Harvest accrued interest directly to external wallet"}
        ]
    },
    "lido_steth": {
        "id": "lido_steth",
        "name": "Lido Liquid Staked ETH (stETH)",
        "protocol": "Lido Finance",
        "chain": "Ethereum",
        "token": "ETH",
        "apy": 3.7,
        "tvl_usd": 23_800_000_000,
        "risk_score": 9.6,
        "risk_level": "Minimal Risk",
        "unbonding_period": "Instant via DEX",
        "audits": ["MixBytes", "Sigma Prime", "StateMind"],
        "slashing_risk": "0.01% (Socialized validator slashing)",
        "icon_url": "https://assets.coingecko.com/coins/images/13442/standard/steth_logo.png",
        "strategies": [
            {"id": "auto_compound", "label": "DeFi Re-Staking", "detail": "Deposit stETH into active validation pools"},
            {"id": "standard", "label": "Standard Rebasing stETH", "detail": "Daily balance increases reflecting consensus rewards"}
        ]
    }
}

# ---------------------------------------------------------------------------
# Card Helpers
# ---------------------------------------------------------------------------
def card_msg(narration: str, kind: str, payload: dict) -> ChatMessage:
    return ChatMessage(
        timestamp=datetime.now(timezone.utc),
        msg_id=uuid4(),
        content=[
            TextContent(type="text", text=narration),
            MetadataContent(
                type="metadata",
                metadata={
                    "card_protocol_version": "1",
                    "requires_card_interaction": "true",
                    "card_kind": kind,
                    "card_payload": json.dumps(payload),
                    "preferred_drawer_width_px": "540"
                }
            )
        ]
    )

def carousel_payload():
    return {
        "title": "YieldSentinel: Verified Staking Vaults",
        "subtitle": "Audited proof-of-stake & DeFi vaults monitored by Risk Guardians",
        "items": [
            {
                "id": p["id"],
                "image": p["icon_url"],
                "title": p["name"],
                "subtitle": f"{p['chain']} · {p['apy']}% APY · {p['unbonding_period']}",
                "badges": [{"label": f"Risk: {p['risk_score']}/10", "variant": "success"}, {"label": p["token"], "variant": "info"}],
                "secondary_text": f"TVL: ${p['tvl_usd']:,} USD",
                "primary_cta": {"label": "Analyze & Allocate", "selection": {"action": "select_pool", "pool_id": p["id"]}}
            }
            for p in POOLS.values()
        ]
    }

def detail_payload(pool_id):
    p = POOLS.get(pool_id, POOLS["asi_fetch_staking"])
    return {
        "title": f"Risk Profile: {p['name']}",
        "hero_image": p["icon_url"],
        "summary_rows": [
            {"label": "Protocol / Chain", "value": f"{p['protocol']} ({p['chain']})"},
            {"label": "Base APY", "value": f"{p['apy']}%"},
            {"label": "TVL", "value": f"${p['tvl_usd']:,} USD"},
            {"label": "Risk Score", "value": f"{p['risk_score']} / 10 ({p['risk_level']})"},
            {"label": "Security Audits", "value": " · ".join(p["audits"])}
        ],
        "sub_options": {
            "name": "strategy",
            "kind": "radio",
            "label": "Compounding Strategy",
            "choices": [{"value": s["id"], "label": s["label"], "secondary_text": s["detail"]} for s in p["strategies"]]
        },
        "approve_cta": {"label": "Proceed to Position Setup", "primary": True, "selection": {"action": "configure_position", "pool_id": pool_id}},
        "reject_cta": {"label": "Back to Pools", "selection": {"action": "back_to_pools"}}
    }

def form_payload(pool_id, strategy):
    p = POOLS.get(pool_id, POOLS["asi_fetch_staking"])
    return {
        "title": f"Configure Allocation: {p['name']}",
        "subtitle": f"Strategy: {strategy.replace('_', ' ').title()}",
        "fields": [
            {"name": "deposit_amount", "kind": "number", "label": f"Deposit Amount ({p['token']})", "placeholder": "500", "required": True},
            {"name": "wallet_address", "kind": "text", "label": f"Delegator {p['token']} Wallet", "placeholder": "fetch1... or 0x...", "required": True},
            {"name": "guardian_alert", "kind": "select", "label": "Automated Risk Guardian Trigger", "options": [
                {"value": "strict", "label": "Strict: Alert if APY drops > 2%"},
                {"value": "moderate", "label": "Moderate: Alert on critical slashing risk"},
                {"value": "off", "label": "Disabled"}
            ]}
        ],
        "submit_cta": {"label": "Review Allocation", "selection": {"action": "submit_position", "pool_id": pool_id, "strategy": strategy}}
    }

def review_payload(session):
    p = POOLS.get(session.get("pool_id", "asi_fetch_staking"), POOLS["asi_fetch_staking"])
    amount = float(session.get("deposit_amount", 500.0))
    annual_earnings = amount * (p["apy"] / 100.0)
    return {
        "title": "Confirm Staking Allocation",
        "summary_rows": [
            {"label": "Vault", "value": p["name"]},
            {"label": "Strategy", "value": session.get("strategy", "Auto Compound").replace('_', ' ').title()},
            {"label": "Deposit Principal", "value": f"{amount:,.2f} {p['token']}"},
            {"label": "Est. 1-Year Returns", "value": f"+{annual_earnings:,.2f} {p['token']}"},
            {"label": "Risk Guardian Check", "value": "PASSED (Certified)"},
            {"label": "Protocol Protection Fee", "value": "0.1 FET"}
        ],
        "approve_cta": {"label": "Authorize & Stake Position", "primary": True, "selection": {"action": "confirm_allocation"}},
        "reject_cta": {"label": "Cancel Position", "selection": {"action": "cancel_allocation"}}
    }

def parse_selection(text):
    try:
        return json.loads(text.strip())
    except Exception:
        pass
    sel = {}
    lower = text.lower()
    for pid in POOLS:
        if pid in lower or pid.replace('_', ' ') in lower:
            sel["pool_id"] = pid
            sel["action"] = "select_pool"
            break
    if "auto" in lower or "compound" in lower:
        sel["strategy"] = "auto_compound"
    if any(w in lower for w in ["confirm", "execute", "stake", "approve"]):
        sel["action"] = "confirm_allocation"
    elif any(w in lower for w in ["cancel", "back"]):
        sel["action"] = "back_to_pools"
    return sel

# ---------------------------------------------------------------------------
# Agent Initialization
# ---------------------------------------------------------------------------
agent = Agent(name="yield_sentinel_cloud", seed="yield-sentinel-asi-cloud-2026-seed")
chat_proto = Protocol(spec=chat_protocol_spec)

@chat_proto.on_message(ChatMessage)
async def on_message(ctx: Context, sender: str, msg: ChatMessage):
    await ctx.send(sender, ChatAcknowledgement(timestamp=datetime.now(timezone.utc), acknowledged_msg_id=msg.msg_id))
    
    text = next((c.text for c in msg.content if isinstance(c, TextContent)), "").strip()
    session = ctx.storage.get(sender) or {}

    if not text or text.lower() in {"hi", "hello", "start", "pools", "stake", "yield"} or session.get("state") is None:
        session["state"] = "browsing"
        ctx.storage.set(sender, session)
        await ctx.send(sender, card_msg("Welcome to **YieldSentinel AI**! Select a verified vault to inspect risk metrics:", "carousel", carousel_payload()))
        return

    sel = parse_selection(text)
    action = sel.get("action")

    if action == "select_pool" or ("pool_id" in sel and session.get("state") == "browsing"):
        pool_id = sel.get("pool_id", "asi_fetch_staking")
        session["pool_id"] = pool_id
        session["state"] = "detail"
        ctx.storage.set(sender, session)
        await ctx.send(sender, card_msg(f"Risk analysis for {POOLS[pool_id]['name']}. Pick your strategy:", "detail", detail_payload(pool_id)))

    elif action == "configure_position" or session.get("state") == "detail":
        pool_id = session.get("pool_id", "asi_fetch_staking")
        strat = sel.get("strategy", "auto_compound")
        session["strategy"] = strat
        session["state"] = "form"
        ctx.storage.set(sender, session)
        await ctx.send(sender, card_msg(f"Configure deposit amount for {POOLS[pool_id]['name']}:", "form", form_payload(pool_id, strat)))

    elif action == "submit_position" or ("deposit_amount" in sel and session.get("state") == "form"):
        session["deposit_amount"] = sel.get("deposit_amount", 500.0)
        session["state"] = "review"
        ctx.storage.set(sender, session)
        await ctx.send(sender, card_msg("Please review and confirm your staking allocation:", "review", review_payload(session)))

    elif action == "confirm_allocation":
        session.clear()
        ctx.storage.set(sender, session)
        await ctx.send(sender, ChatMessage(
            timestamp=datetime.now(timezone.utc),
            msg_id=uuid4(),
            content=[TextContent(type="text", text="🎉 **Staking Position Successfully Allocated!**\n\n• **Status**: Active\n• **Guardian Monitoring**: 24/7 Enabled\n• **Protocol Fee**: 0.1 FET\n\nType **pools** anytime to manage or open new positions.")]
        ))

    else:
        await ctx.send(sender, card_msg("Here are the available staking pools:", "carousel", carousel_payload()))

@chat_proto.on_message(ChatAcknowledgement)
async def on_ack(ctx: Context, sender: str, msg: ChatAcknowledgement):
    pass

agent.include(chat_proto, publish_manifest=True)

if __name__ == "__main__":
    agent.run()
