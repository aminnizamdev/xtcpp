# xtcpp_3.py – Insight Display

import sys
import os
import socket
import json
from rich.console import Console
from rich.table import Table

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from shared.config import XTCPP_PORTS

RECEIVE_PORT = XTCPP_PORTS["2_to_3"]
console = Console()
insight_log = []

def display_table():
    table = Table(title="XTCPP_3 – Wallet Insight Dashboard")
    table.add_column("Wallet", style="cyan")
    table.add_column("Tag", style="magenta")
    table.add_column("Balance", style="green")
    table.add_column("Last Seen", style="yellow")
    table.add_column("Notes", style="white")

    for insight in insight_log[-10:]:
        table.add_row(
            insight["wallet"][:6] + "..." + insight["wallet"][-4:],
            insight["tag"],
            insight["balance"],
            insight["last_seen"],
            insight["notes"]
        )
    console.clear()
    console.print(table)

def start_display_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("127.0.0.1", RECEIVE_PORT))
        server.listen()
        console.log(f"XTCPP_3 listening on TCP port {RECEIVE_PORT}...")

        while True:
            conn, _ = server.accept()
            with conn:
                data = conn.recv(4096)
                if data:
                    try:
                        insight = json.loads(data.decode("utf-8"))
                        insight_log.append(insight)
                        display_table()
                    except Exception as e:
                        console.log(f"[DISPLAY ERROR] {e}")

if __name__ == "__main__":
    start_display_server()
