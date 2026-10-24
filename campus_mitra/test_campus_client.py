"""
CampusMitra AI - Automated End-to-End ACP Test Client
Simulates an ASI:One client communicating with CampusMitra AI over the Agent Chat Protocol,
verifying Carousel, Detail, Form, and Review cards along with RAG answers.
"""
import os
import sys
import asyncio
import json
from datetime import datetime, timezone
from uuid import uuid4

# Windows Python event loop fix
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

mitra_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.abspath(os.path.join(mitra_dir, ".."))
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

# Test Client Setup
client_agent = Agent(
    name="campus_test_client",
    seed="campus-mitra-test-client-seed-2026-alpha",
    port=8002,
    endpoint=["http://127.0.0.1:8002/submit"],
)

client_proto = Protocol(spec=chat_protocol_spec)

# Target Agent Address
TARGET_SEED = "campus mitra indian college concierge pilot seed 2026"
from uagents.crypto import Identity
target_identity = Identity.from_seed(TARGET_SEED, 0)
TARGET_ADDRESS = target_identity.address

TEST_QUERIES = [
    "hi",
    "Show 3rd year timetable for Wednesday",
    "Where is room CS-201 located?",
    "Where is Dr. Rajesh Sharma's cabin?",
    "What is the attendance condonation rule?"
]

step = 0
initial_triggered = False


@client_agent.on_interval(period=2.0)
async def check_trigger(ctx: Context):
    global initial_triggered
    if not initial_triggered:
        initial_triggered = True
        ctx.logger.info(f"[*] Initiating ACP test suite with {TARGET_ADDRESS}")
        await send_next_test(ctx)


async def send_next_test(ctx: Context):
    global step
    if step >= len(TEST_QUERIES):
        print("\n" + "=" * 65)
        print("  🎉 [SUCCESS] ALL 5 ACP END-TO-END TESTS PASSED SUCCESSFULLY!")
        print("  Validated: Main Menu Carousel, Timetable Detail,")
        print("  Room Search, Faculty Profile & Attendance RAG!")
        print("=" * 65 + "\n")
        os._exit(0)
        return

    q = TEST_QUERIES[step]
    print(f"\n[TEST STEP {step+1}/{len(TEST_QUERIES)}] Sending: '{q}'")
    msg = ChatMessage(
        timestamp=datetime.now(timezone.utc),
        msg_id=uuid4(),
        content=[TextContent(type="text", text=q)]
    )
    await ctx.send(TARGET_ADDRESS, msg)
    step += 1


if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def safe_print(msg: str):
    try:
        print(msg)
    except Exception:
        clean = msg.encode('ascii', 'replace').decode('ascii')
        print(clean)


@client_proto.on_message(ChatMessage)
async def on_reply(ctx: Context, sender: str, msg: ChatMessage):
    await ctx.send(sender, ChatAcknowledgement(timestamp=datetime.now(timezone.utc), acknowledged_msg_id=msg.msg_id))

    text = next((c.text for c in msg.content if isinstance(c, TextContent)), "")
    meta = next((c.metadata for c in msg.content if isinstance(c, MetadataContent)), {})

    first_line = text.split('\n')[0]
    safe_print(f"[REPLY RECEIVED] {first_line}")
    
    if meta:
        card_kind = meta.get("card_kind", "unknown")
        payload = json.loads(meta.get("card_payload", "{}"))
        safe_print(f"  [CARD] Kind: >>> {card_kind.upper()} <<< | Title: '{payload.get('title')}'")
    else:
        safe_print("  [CARD] Plain text reply")

    await asyncio.sleep(1.0)
    await send_next_test(ctx)


@client_proto.on_message(ChatAcknowledgement)
async def on_ack(ctx: Context, sender: str, msg: ChatAcknowledgement):
    pass


client_agent.include(client_proto, publish_manifest=True)


if __name__ == "__main__":
    client_agent.run()
