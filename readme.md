# XTCPP – XRP Terminal Client with Python Power

<div align="center">

![XTCPP Banner](https://via.placeholder.com/800x200.png?text=XTCPP)

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![XRPL](https://img.shields.io/badge/Network-XRPL-blue.svg)](https://xrpl.org/)
[![CLI Native](https://img.shields.io/badge/CLI-Native-green.svg)](https://github.com/aminnizamdev/xtcpp)

**A modular agent system for real-time XRP Ledger monitoring and analysis**

[Features](#features) • [Architecture](#architecture) • [Installation](#installation) • [Running XTCPP](#running-xtcpp) • [Configuration](#configuration) • [Tech Stack](#tech-stack) • [Use Cases](#use-cases)

</div>

## Overview

XTCPP is a powerful CLI-native modular agent system that monitors the XRP Ledger in real-time. It filters whale transactions, analyzes wallet behavior, and displays symbolic insights through an elegant terminal-based interface. The system is composed of four interconnected Python agents, each with a specific responsibility in the monitoring and analysis pipeline.

## Features

- **Real-time XRP Ledger Monitoring**: Connect directly to the XRPL WebSocket API
- **Whale Transaction Detection**: Automatically identify and track large XRP movements
- **Wallet Analysis**: Extract and categorize wallet behavior patterns
- **Live Terminal Dashboard**: View insights and transaction data in real-time
- **Modular Architecture**: Distributed processing across specialized agents
- **Low Latency**: Optimized for real-time transaction monitoring
- **Symbolic Insights**: Advanced pattern recognition for wallet activity

## Architecture

XTCPP utilizes a multi-agent architecture with TCP socket communication between specialized components:

### XTCPP_0: Mother Server

- Connects to `wss://s1.ripple.com` WebSocket endpoint
- Streams all XRP Ledger transactions in real-time
- Filters whale transactions (≥ 1M XRP payments)
- Forwards significant transactions via TCP loopback (port 8001)

### XTCPP_1: Whale Watcher

- Listens on TCP port 8001 for incoming whale transactions
- Displays whale transaction details with rich formatting
- Extracts source and destination wallet addresses
- Forwards wallet information to XTCPP_2 via TCP (port 8002)

### XTCPP_2: Wallet Analyzer

- Receives wallet addresses for analysis
- Queries the XRPL WebSocket API for detailed account information
- Tags wallets with classifications (e.g., "Dormant Whale", "Standard Wallet")
- Sends analytical insights to XTCPP_3 via TCP (port 8003)

### XTCPP_3: Insight Display

- Creates a rich terminal dashboard for monitoring wallet insights
- Displays wallet tags, balances, and transaction context
- Provides an at-a-glance view of significant XRPL activity

## Project Structure

```
xtcpp/
├── agents/
│   ├── xtcpp_0.py       # Mother Server
│   ├── xtcpp_1.py       # Whale Watcher
│   ├── xtcpp_2.py       # Wallet Analyzer
│   └── xtcpp_3.py       # Insight Display
├── shared/
│   ├── config.py        # System configuration
│   ├── types.py         # Type definitions
│   └── utils.py         # Shared utilities
├── launcher.bat         # Windows launcher script
└── requirements.txt     # Python dependencies
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Windows OS (for the launcher script, though agents can run on any OS)
- Internet connection to access the XRP Ledger

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/aminnizamdev/xtcpp.git
   cd xtcpp
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running XTCPP

### Using the Launcher (Windows)

Simply run the included launcher script:

```bash
launcher.bat
```

This will start all four agents in separate command windows.

### Manual Launch

For more control or non-Windows environments, launch each agent separately:

```bash
# Start each agent in a different terminal
python agents/xtcpp_0.py
python agents/xtcpp_1.py
python agents/xtcpp_2.py
python agents/xtcpp_3.py
```

## Configuration

XTCPP can be configured through the `shared/config.py` file:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `XTCPP_PORTS` | TCP ports for inter-agent communication | `8001, 8002, 8003` |
| `XRPL_WEBSOCKET_URL` | WebSocket endpoint for the XRP Ledger | `wss://s1.ripple.com` |
| `WHALE_THRESHOLD_XRP` | Minimum XRP amount to trigger whale detection | `1,000,000` |
| `VERBOSE` | Enable additional debugging output | `True` |

## Tech Stack

- **Python 3.8+**: Core programming language
- **Websockets**: For connecting to the XRP Ledger API
- **Rich**: Terminal formatting and dashboard creation
- **TCP Sockets**: Inter-agent communication
- **XRP Ledger API**: Data source for blockchain transactions

## Data Flow

```
XRP Ledger API → XTCPP_0 → XTCPP_1 → XTCPP_2 → XTCPP_3
                  ↓          ↓          ↓          ↓
            All Transaction  Whale     Wallet    Insight
             Monitoring     Detection  Analysis  Dashboard
```

## Use Cases

- **Cryptocurrency Research**: Monitor large XRP movements for market analysis
- **Whale Activity Tracking**: Identify patterns in significant holder behavior
- **Wallet Profiling**: Understand characteristics of active XRP wallets
- **Market Signal Detection**: Spot potential market-moving transactions early
- **Network Health Monitoring**: Observe transaction volumes and patterns
- **Investment Strategy Insights**: Inform trading decisions with real-time data

## Future Development

- **Additional Blockchains**: Extend monitoring to other cryptocurrency networks
- **Machine Learning Integration**: Enhance wallet classification and pattern detection
- **Alert System**: Push notifications for critical transaction patterns
- **Historical Analysis**: Compare current activity against historical patterns
- **API Interface**: Allow other applications to consume XTCPP insights

## License

This project is available under the MIT License.

## Acknowledgments

- XRP Ledger Foundation for providing the public WebSocket API
- Python open-source community for the excellent libraries

---

<div align="center">

**[GitHub](https://github.com/aminnizamdev/xtcpp) • [Report Issues](https://github.com/aminnizamdev/xtcpp/issues) • [XRP Ledger](https://xrpl.org/)**

*Developed by [Amin Nizam](https://github.com/aminnizamdev)*

</div>
