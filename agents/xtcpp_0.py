# xtcpp_0.py - Mother Server

import sys
import os

# Ensure 'shared/' can be imported properly regardless of launch context
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

import asyncio
import json
import socket
from datetime import datetime

import websockets
from rich.console import Console
from shared.config import XRPL_WEBSOCKET_URL, XTCPP_PORTS, WHALE_THRESHOLD_XRP, VERBOSE

console = Console()
WHALE_PORT = XTCPP_PORTS["0_to_1"]

def drops_to_xrp(drops):
    try:
        return int(drops) / 1_000_000
    except:
        return 0

def format_tx(tx):
    amount_drops = tx.get("Amount", "0")
    xrp = drops_to_xrp(amount_drops)
    from_addr = tx.get("Account", "")[:6] + "..." + tx.get("Account", "")[-4:]
    to_addr = tx.get("Destination", "")[:6] + "..." + tx.get("Destination", "")[-4:]
    return f"[{datetime.now().strftime('%H:%M:%S')}] Payment | {xrp:,.0f} XRP | From: {from_addr} | To: {to_addr}"

async def send_to_tcp(recipient_json: dict):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect(("127.0.0.1", WHALE_PORT))
            sock.sendall(json.dumps(recipient_json).encode("utf-8"))
    except Exception as e:
        if VERBOSE:
            console.log(f"[TCP SEND ERROR] {e}")

async def listen_to_xrpl():
    try:
        async with websockets.connect(XRPL_WEBSOCKET_URL) as ws:
            await ws.send(json.dumps({
                "id": 1,
                "command": "subscribe",
                "streams": ["transactions"]
            }))

            console.log("XTCPP_0 connected to XRPL WebSocket. Listening...")
            while True:
                try:
                    msg = await ws.recv()
                    data = json.loads(msg)
                    tx = data.get("transaction", {})
                    if tx.get("TransactionType") != "Payment":
                        continue

                    # Display all payment transactions
                    console.print(format_tx(tx))

                    # Whale filter
                    amount = drops_to_xrp(tx.get("Amount", "0"))
                    if amount >= WHALE_THRESHOLD_XRP:
                        whale_tx = {
                            "from": tx.get("Account"),
                            "to": tx.get("Destination"),
                            "amount": str(amount),
                            "timestamp": datetime.now().isoformat()
                        }
                        await send_to_tcp(whale_tx)

                except Exception as inner:
                    console.log(f"[ERROR] {inner}")
                    await asyncio.sleep(2)
    except Exception as outer:
        console.log(f"[CONNECTION FAILED] {outer}")

if __name__ == "__main__":
    asyncio.run(listen_to_xrpl())
