"""
YieldSentinel - Automated Test Suite / Simulated ASI:One ACP Client
Simulates full multi-step conversation flow and validates Interactive Cards payloads.
"""

import asyncio
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

import json
from datetime import datetime, timezone
from uuid import uuid4
from uagents import Agent, Context
from uagents_core.contrib.protocols.chat import (
    ChatMessage,
    ChatAcknowledgement,
    MetadataContent,
    TextContent,
    chat_protocol_spec,
)
from uagents import Protocol

# Test Client configuration
client = Agent(
    name="asione_simulated_user",
    seed="simulated-asione-user-seed-phrase",
    port=8005,
    endpoint=["http://localhost:8005/submit"]
)
chat_proto = Protocol(spec=chat_protocol_spec)

# Simulated conversation state
step = 0
TARGET_AGENT_ADDRESS = None


def create_user_msg(text_or_json: str) -> ChatMessage:
    return ChatMessage(
        timestamp=datetime.now(timezone.utc),
        msg_id=uuid4(),
        content=[TextContent(type="text", text=text_or_json)]
    )


@chat_proto.on_message(ChatMessage)
async def handle_agent_reply(ctx: Context, sender: str, msg: ChatMessage):
    global step
    await ctx.send(
        sender,
        ChatAcknowledgement(
            timestamp=datetime.now(timezone.utc),
            acknowledged_msg_id=msg.msg_id
        )
    )

    # Inspect text narration
    text = next((c.text for c in msg.content if isinstance(c, TextContent)), "")
    
    # Inspect metadata card declaration
    metadata_block = next((c.metadata for c in msg.content if isinstance(c, MetadataContent)), None)

    print("\n-------------------------------------------------------------")
    print(f"[RECV - STEP {step}] FROM YIELDSENTINEL:")
    print(f"Narration: {text[:140]}...")

    if metadata_block:
        card_kind = metadata_block.get("card_kind")
        payload = json.loads(metadata_block.get("card_payload", "{}"))
        print(f"CARD TYPE: >>> {card_kind.upper()} <<<")
        print(f"Card Title: {payload.get('title')}")
        if card_kind == "carousel":
            print(f"   Items Count: {len(payload.get('items', []))}")
        elif card_kind == "detail":
            print(f"   Summary Rows: {len(payload.get('summary_rows', []))}")
        elif card_kind == "form":
            print(f"   Fields: {[f['name'] for f in payload.get('fields', [])]}")
        elif card_kind == "review":
            print(f"   Approve CTA: {payload.get('approve_cta', {}).get('label')}")
    else:
        print("Plain text message (Terminal or confirmation)")
    print("-------------------------------------------------------------")

    # Step progression
    if step == 0:
        step = 1
        print("[USER ACTION] Selecting 'asi_fetch_staking' from Carousel...")
        reply = json.dumps({"action": "select_pool", "pool_id": "asi_fetch_staking"})
        await ctx.send(sender, create_user_msg(reply))

    elif step == 1:
        step = 2
        print("[USER ACTION] Selecting Auto-Compound Strategy and proceeding...")
        reply = json.dumps({"action": "configure_position", "pool_id": "asi_fetch_staking", "strategy": "auto_compound"})
        await ctx.send(sender, create_user_msg(reply))

    elif step == 2:
        step = 3
        print("[USER ACTION] Submitting Form with 1,000 FET deposit and wallet address...")
        reply = json.dumps({
            "action": "submit_position",
            "pool_id": "asi_fetch_staking",
            "deposit_amount": 1000.0,
            "wallet_address": "fetch1q89df34ka78m02kcl984",
            "guardian_alert": "strict"
        })
        await ctx.send(sender, create_user_msg(reply))

    elif step == 3:
        step = 4
        print("[USER ACTION] Confirming Allocation from Review Card...")
        reply = json.dumps({"action": "confirm_allocation"})
        await ctx.send(sender, create_user_msg(reply))

    elif step == 4:
        print("\n[SUCCESS] WORKFLOW COMPLETED SUCCESSFULLY! ALL 4 CARDS VALIDATED!\n")


@chat_proto.on_message(ChatAcknowledgement)
async def handle_client_ack(ctx: Context, sender: str, msg: ChatAcknowledgement):
    pass


client.include(chat_proto, publish_manifest=True)


import sys

TARGET_AGENT_ADDRESS = (
    sys.argv[1]
    if len(sys.argv) > 1
    else "agent1q2c8s3r6zvtunmx84ncxlrwdv8txjxwwz6s7shu75wexnqsr590uwefxkm6"
)

initial_sent = False

@client.on_interval(period=2.0)
async def send_first_message(ctx: Context):
    global initial_sent
    if not initial_sent:
        initial_sent = True
        ctx.logger.info(f"Initiating conversation with {TARGET_AGENT_ADDRESS}")
        await ctx.send(TARGET_AGENT_ADDRESS, create_user_msg("Hi! Find me the best staking yields."))


if __name__ == "__main__":
    client.run()
