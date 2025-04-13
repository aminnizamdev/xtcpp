# xtcpp_1.py – Whale Watcher

import sys
import os

# Make shared/ accessible
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

import socket
import threading
import json
from rich.console import Console
from datetime import datetime

from shared.config import XTCPP_PORTS, VERBOSE

console = Console()

RECEIVE_PORT = XTCPP_PORTS["0_to_1"]  # from xtcpp_0
SEND_PORT = XTCPP_PORTS["1_to_2"]     # to xtcpp_2

# === UTILITY ===
def shorten(addr):
    return addr[:6] + "..." + addr[-4:]

def send_wallet_payload(wallet_payload):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("127.0.0.1", SEND_PORT))
            s.sendall(json.dumps(wallet_payload).encode("utf-8"))
            if VERBOSE:
                console.log(f"→ Sent to XTCPP_2: {wallet_payload}")
    except Exception as e:
        if VERBOSE:
            console.log(f"[SEND ERROR] {e}")

def handle_whale_tx(msg):
    try:
        tx = json.loads(msg)
        from_addr = tx.get("from", "")
        to_addr = tx.get("to", "")
        amount = tx.get("amount", "?")
        ts = tx.get("timestamp", "")

        # === Display in terminal ===
        console.print(f"[{datetime.now().strftime('%H:%M:%S')}] [Whale] {amount} XRP | From: {shorten(from_addr)} | To: {shorten(to_addr)}")

        # === Silent forwarding ===
        wallet_data = {
            "from": from_addr,
            "to": to_addr,
            "amount": amount,
            "ts": ts
        }
        send_wallet_payload(wallet_data)

    except Exception as e:
        console.log(f"[TX PARSE ERROR] {e}")

def start_whale_receiver():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("127.0.0.1", RECEIVE_PORT))
        server.listen()
        console.log(f"XTCPP_1 listening on TCP port {RECEIVE_PORT}...")

        while True:
            conn, _ = server.accept()
            with conn:
                msg = conn.recv(4096)
                if msg:
                    handle_whale_tx(msg.decode("utf-8"))

if __name__ == "__main__":
    start_whale_receiver()
