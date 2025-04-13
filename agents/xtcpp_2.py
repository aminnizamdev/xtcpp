# xtcpp_2.py – Wallet Analyzer

import sys
import os
import asyncio
import json
import socket
from datetime import datetime

import websockets
from rich.console import Console

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from shared.config import XTCPP_PORTS, XRPL_WEBSOCKET_URL, VERBOSE

RECEIVE_PORT = XTCPP_PORTS["1_to_2"]
SEND_PORT = XTCPP_PORTS["2_to_3"]

console = Console()
seen_wallets = set()

async def query_wallet(wallet_address):
    payload = {
        "id": 1,
        "command": "account_info",
        "account": wallet_address,
        "strict": True,
        "ledger_index": "validated"
    }

    try:
        async with websockets.connect(XRPL_WEBSOCKET_URL) as ws:
            await ws.send(json.dumps(payload))
            response = await ws.recv()
            return json.loads(response)
    except Exception as e:
        if VERBOSE:
            console.log(f"[WS ERROR] {e}")
        return None

def tag_wallet(account_data):
    try:
        balance = int(account_data["account_data"]["Balance"]) / 1_000_000
        last_ledger = account_data["account_data"]["LedgerEntryType"]
        tag = "Dormant Whale" if balance >= 1_000_000 else "Standard Wallet"
        return tag, balance
    except:
        return "Unknown", 0

def send_to_xtcpp3(insight):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("127.0.0.1", SEND_PORT))
            s.sendall(json.dumps(insight).encode("utf-8"))
    except Exception as e:
        if VERBOSE:
            console.log(f"[SEND FAIL → XTCPP_3] {e}")

async def handle_wallet(from_addr, to_addr, amount, ts):
    for wallet in [from_addr, to_addr]:
        if wallet in seen_wallets:
            continue
        seen_wallets.add(wallet)

        response = await query_wallet(wallet)
        if not response or "account_data" not in response.get("result", {}):
            continue

        tag, balance = tag_wallet(response["result"])
        insight = {
            "wallet": wallet,
            "tag": tag,
            "balance": f"{balance:,.2f} XRP",
            "last_seen": ts,
            "notes": f"Processed due to {amount} XRP transfer"
        }

        send_to_xtcpp3(insight)
        console.log(f"Tagged: {wallet[:6]}... → {tag}")

def start_tcp_receiver():
    async def handler():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("127.0.0.1", RECEIVE_PORT))
            server.listen()
            console.log(f"XTCPP_2 listening on TCP port {RECEIVE_PORT}...")

            while True:
                conn, _ = server.accept()
                with conn:
                    data = conn.recv(4096)
                    if data:
                        try:
                            payload = json.loads(data.decode("utf-8"))
                            await handle_wallet(payload["from"], payload["to"], payload["amount"], payload["ts"])
                        except Exception as e:
                            console.log(f"[HANDLE ERROR] {e}")

    asyncio.run(handler())

if __name__ == "__main__":
    start_tcp_receiver()
