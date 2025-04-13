# shared/config.py

# Port map for TCP loopback between agents
XTCPP_PORTS = {
    "0_to_1": 8001,  # Whale tx from Mother Server
    "1_to_2": 8002,  # Wallets from Whale Watcher
    "2_to_3": 8003,  # Symbolic insights to Display Agent
}

# Public Ripple WebSocket API
XRPL_WEBSOCKET_URL = "wss://s1.ripple.com"

# Threshold for whale detection (in XRP)
WHALE_THRESHOLD_XRP = 1_000_000

# Enable debug logs and internal tracing
VERBOSE = True
