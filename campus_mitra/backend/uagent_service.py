"""
CampusMitra AI - Fetch.ai uAgent with Agent Chat Protocol (ACP)
Listens for ASI:One messages, runs the Multi-Agent LangGraph/Python orchestrator,
and emits responses formatted with ASI Interactive Cards protocol.
"""
import os
import sys
import asyncio
from datetime import datetime, timezone
from uuid import uuid4

# Windows Python event loop fix
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Ensure paths
current_dir = os.path.dirname(os.path.abspath(__file__))
mitra_dir = os.path.abspath(os.path.join(current_dir, ".."))
workspace_dir = os.path.abspath(os.path.join(current_dir, "..", ".."))
for p in [mitra_dir, workspace_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

from uagents import Agent, Context, Protocol
from uagents_core.contrib.protocols.chat import (
    ChatAcknowledgement,
    ChatMessage,
    MetadataContent,
    TextContent,
    chat_protocol_spec,
)

from backend.agents.orchestrator import CampusMitraOrchestrator
from backend.cards.card_builder import create_card_msg

# Configuration
AGENT_SEED = os.getenv("CAMPUS_AGENT_SEED", "campus mitra indian college concierge pilot seed 2026")
AGENT_PORT = int(os.getenv("UAGENT_PORT", 8000))

campus_agent = Agent(
    name="campus_mitra_ai",
    seed=AGENT_SEED,
    port=AGENT_PORT,
    endpoint=[f"http://127.0.0.1:{AGENT_PORT}/submit"],
)

chat_proto = Protocol(spec=chat_protocol_spec)
orchestrator = CampusMitraOrchestrator()


@chat_proto.on_message(ChatMessage)
async def on_chat_message(ctx: Context, sender: str, msg: ChatMessage):
    # 1. Immediate ACP Acknowledgement
    ack = ChatAcknowledgement(
        timestamp=datetime.now(timezone.utc),
        acknowledged_msg_id=msg.msg_id
    )
    await ctx.send(sender, ack)
    ctx.logger.info(f"[ACP ACK] Sent ack to {sender} for msg {msg.msg_id}")

    # 2. Extract Text Content
    text = next((c.text for c in msg.content if isinstance(c, TextContent)), "").strip()
    session = ctx.storage.get(sender) or {}

    ctx.logger.info(f"[ACP INCOMING] From: {sender} | Text: '{text}'")

    # 3. Process via Multi-Agent Orchestrator
    result = orchestrator.process_request(text, session)

    # 4. Save Session
    new_session = {**session, **result.get("session_updates", {})}
    ctx.storage.set(sender, new_session)

    # 5. Format ASI Interactive Card Response
    reply_card_msg = create_card_msg(
        narration=result["text"],
        kind=result["card_kind"],
        payload=result["card_payload"]
    )
    await ctx.send(sender, reply_card_msg)
    ctx.logger.info(f"[ACP REPLY] Dispatched {result['card_kind']} card from {result['agent_used']} to {sender}")


@chat_proto.on_message(ChatAcknowledgement)
async def on_chat_ack(ctx: Context, sender: str, msg: ChatAcknowledgement):
    ctx.logger.info(f"[ACP ACK RECEIVED] From {sender} for msg {msg.acknowledged_msg_id}")


# Include Protocol
campus_agent.include(chat_proto, publish_manifest=True)


if __name__ == "__main__":
    print(f"[*] Starting CampusMitra AI Agent on port {AGENT_PORT}...")
    print(f"[*] Agent Address: {campus_agent.address}")
    campus_agent.run()
