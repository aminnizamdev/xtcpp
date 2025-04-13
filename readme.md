<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=XTCPP&fontSize=80&fontAlignY=35&animation=fadeIn&desc=XRP%20Terminal%20Client%20with%20Python%20Power&descSize=25&descAlignY=50&fontColor=white" alt="XTCPP Banner">

  ![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)
  ![WebSockets](https://img.shields.io/badge/WebSockets-API-25c2a0?logo=websocket&logoColor=white)
  ![CLI](https://img.shields.io/badge/CLI-Native-black?logo=windowsterminal&logoColor=white)
  ![XRP](https://img.shields.io/badge/XRP-Ledger-23D09F?logo=xrp&logoColor=white)
  ![Rich](https://img.shields.io/badge/Rich-TUI-71638D?logo=python&logoColor=white)
  
  <h4>A modular multi-agent system for real-time XRP Ledger monitoring and whale transaction analysis</h4>
</div>

## 🌊 Overview

XTCPP (XRP Terminal Client with Python Power) is a high-performance, CLI-native system that monitors the XRP Ledger in real-time, focusing on tracking "whale" transactions (movements of ≥1M XRP) across the network. The system filters whale movements, analyzes wallet behaviors, and provides symbolic insights through a multi-agent architecture communicating via TCP loopback connections.

<div align="center">
  <img src="https://img.shields.io/badge/Multi--Agent-Architecture-FF6384?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiwxQzUuMzgsMSAxLDUuMzggMSwxMkMxLDE4LjYyIDUuMzgsMjMgMTIsMjNDMTguNjIsMjMgMjMsMTguNjIgMjMsMTJDMjMsNS4zOCAxOC42MiwxIDEyLDFNMTIsMTlDOC4xMywxOSA1LDE1Ljg3IDUsMTJDNSw4LjEzIDguMTMsNSAxMiw1QzE1Ljg3LDUgMTksOC4xMyAxOSwxMkMxOSwxNS44NyAxNS44NywxOSAxMiwxOU0xMiw3QzEwLjEsNyA4LjUsOC4zOCA4LjUsMTBDOC41LDEwLjE5IDguNjQsMTAuMzMgOC44MywxMC4zM0g5QzEwLjE3LDEwLjMzIDExLjE3LDEwLjg5IDExLjE3LDEyLjA2QzExLjE3LDEzLjIyIDEwLjE3LDEzLjgzIDksMTMuODNDOC44MSwxMy44MyA4LjY3LDEzLjk3IDguNjcsMTQuMTZWMTUuMTdDOC42NywxNS4zNiA4LjgxLDE1LjUgOSwxNS41SDEwLjE3QzEwLjM1LDE1LjUgMTAuNSwxNS4zNiAxMC41LDE1LjE3VjE0QzEwLjUsMTMuODEgMTAuMzUsMTMuNjcgMTAuMTcsMTMuNjdDOS41LDEzLjY3IDksMTMuNDYgOSwxMkM5LDExIDE0LDExIDE0LDhDMTQsNy4zOSAxMy44LDcgMTMuNjcsN0gxMloiLz48L3N2Zz4=" alt="Multi-Agent">
</div>

## 🧠 Architecture

XTCPP employs a specialized four-agent system, each with distinct responsibilities:

<div align="center">
  <table>
    <tr>
      <th align="center">Agent</th>
      <th align="center">Role</th>
      <th align="center">Input</th>
      <th align="center">Output</th>
    </tr>
    <tr>
      <td align="center"><b>XTCPP_0</b><br>Mother Server</td>
      <td>Connects directly to the XRP Ledger WebSocket API, filtering and capturing all transaction data</td>
      <td>XRPL WebSocket Feed</td>
      <td>Filtered whale transactions</td>
    </tr>
    <tr>
      <td align="center"><b>XTCPP_1</b><br>Whale Watcher</td>
      <td>Processes whale transactions (≥1M XRP) and identifies originating/destination wallets</td>
      <td>Whale transactions from XTCPP_0</td>
      <td>Wallet addresses</td>
    </tr>
    <tr>
      <td align="center"><b>XTCPP_2</b><br>Wallet Analyzer</td>
      <td>Queries the XRPL for additional wallet data, classifies wallets by behavior and characteristics</td>
      <td>Wallet addresses from XTCPP_1</td>
      <td>Wallet insights</td>
    </tr>
    <tr>
      <td align="center"><b>XTCPP_3</b><br>Insight Display</td>
      <td>Renders detailed wallet analysis in a terminal UI for real-time monitoring</td>
      <td>Wallet insights from XTCPP_2</td>
      <td>Terminal dashboard</td>
    </tr>
  </table>
</div>

## 🔄 Data Flow

The system's data flow operates in a cascading pattern:

```
XRP Ledger 
   ↓ [WebSocket API]
XTCPP_0 (Mother Server) ← All Transactions
   ↓ [TCP port 8001]  ← Filtered for ≥1M XRP
XTCPP_1 (Whale Watcher)
   ↓ [TCP port 8002]  ← Wallet addresses extracted
XTCPP_2 (Wallet Analyzer)
   ↓ [TCP port 8003]  ← Wallet tagging and classification
XTCPP_3 (Insight Display)
   ↓ [Terminal UI]
Rich Terminal Dashboard
```

## 🚀 Key Features

- **Real-time XRPL Monitoring**: Direct connection to the XRP Ledger's primary WebSocket endpoint
- **Configurable Whale Detection**: Customizable threshold (default: 1M XRP)
- **Multi-Agent Architecture**: Modular design with each agent focusing on a specific task
- **Wallet Classification**: Automatic tagging and classification of XRP wallets
- **Rich Terminal UI**: High-quality terminal dashboard built with the Rich library
- **Low Resource Footprint**: Efficient Python implementation requiring minimal system resources
- **Zero-DB Design**: No database dependencies - pure in-memory processing

## 💻 Technical Implementation

XTCPP utilizes several key technologies:

- **Python 3.8+**: Core language providing cross-platform capabilities
- **WebSockets**: Asynchronous connection to the XRP Ledger
- **TCP Loopback**: Inter-agent communication via network sockets
- **Rich Library**: Terminal UI enhancements for data presentation
- **Dataclasses**: Type-hinted data structures for transaction processing

## 🔧 Setup & Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/xtcpp.git
   cd xtcpp
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the system:
   ```bash
   # On Windows
   launcher.bat
   
   # On Linux/macOS
   python agents/xtcpp_0.py &
   python agents/xtcpp_1.py &
   python agents/xtcpp_2.py &
   python agents/xtcpp_3.py &
   ```

## 📊 Usage Scenarios

XTCPP is designed for several specific use cases:

- **Whale Movement Analysis**: Track large-scale movements of XRP that may influence market dynamics
- **Market Research**: Identify patterns in institutional/large holder behaviors on the XRP Ledger
- **Network Monitoring**: Observe XRP Ledger health and transaction flows in real-time
- **Wallet Classification**: Build knowledge about wallet behaviors and transaction patterns

## 📁 Project Structure

```
xtcpp/
├── agents/                # Agent implementation files
│   ├── xtcpp_0.py        # Mother Server - XRPL connection
│   ├── xtcpp_1.py        # Whale Watcher - Transaction processor
│   ├── xtcpp_2.py        # Wallet Analyzer - XRPL account queries
│   └── xtcpp_3.py        # Insight Display - Terminal UI
├── shared/               # Shared resources and utilities
│   ├── config.py         # System configuration and constants
│   ├── types.py          # Data structure definitions
│   └── utils.py          # Helper functions
├── launcher.bat          # Windows launcher script
└── requirements.txt      # Python dependencies
```

## ⚙️ Configuration

The system can be configured by modifying the `shared/config.py` file:

```python
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
```

## 📝 Implementation Details

### WebSocket Connection

The system establishes a direct WebSocket connection to the XRP Ledger:

```python
async with websockets.connect(XRPL_WEBSOCKET_URL) as ws:
    await ws.send(json.dumps({
        "id": 1,
        "command": "subscribe",
        "streams": ["transactions"]
    }))
```

### Whale Transaction Detection

Transactions are filtered based on the configured threshold:

```python
amount = drops_to_xrp(tx.get("Amount", "0"))
if amount >= WHALE_THRESHOLD_XRP:
    whale_tx = {
        "from": tx.get("Account"),
        "to": tx.get("Destination"),
        "amount": str(amount),
        "timestamp": datetime.now().isoformat()
    }
    await send_to_tcp(whale_tx)
```

### Wallet Analysis

The system queries the XRPL API for wallet information:

```python
payload = {
    "id": 1,
    "command": "account_info",
    "account": wallet_address,
    "strict": True,
    "ledger_index": "validated"
}

async with websockets.connect(XRPL_WEBSOCKET_URL) as ws:
    await ws.send(json.dumps(payload))
    response = await ws.recv()
    return json.loads(response)
```

### Inter-Agent Communication

Agents communicate via TCP sockets on localhost:

```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", SEND_PORT))
    s.sendall(json.dumps(wallet_payload).encode("utf-8"))
```

## 🛠️ Extending XTCPP

XTCPP can be extended in several ways:

1. **Additional Analyzers**: Create new agents that connect to existing data flows
2. **Enhanced Classification**: Improve wallet tagging with more sophisticated rules
3. **Historical Storage**: Add database integration for persistent storage
4. **Alert System**: Implement notification services for specific events
5. **Web Interface**: Develop a browser-based dashboard

## 📜 License

This project is open-source and available under the MIT License.

## 🙏 Acknowledgements

- The XRP Ledger Foundation for providing public WebSocket endpoints
- The Rich library for terminal UI capabilities
- Python Websockets library for asynchronous WebSocket connections

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer&animation=fadeIn" alt="footer">
  <p>
    <img src="https://img.shields.io/badge/Made%20with%20%E2%99%A5%20by-Amin%20Mohamad%20Nizam-blue?style=for-the-badge" alt="Made with love">
  </p>
  <p>
    <img src="https://img.shields.io/badge/Last%20Updated-April%202025-lightgrey?style=flat-square" alt="Last Updated">
  </p>
</div>
