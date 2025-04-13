# XTCPP – XRP Terminal Client with Python Power

XTCPP is a CLI-native modular agent system that monitors the XRP Ledger in real time,
filters whale transactions, analyzes wallet behavior, and displays symbolic insights.

---

## 🧠 Architecture Overview

1. **XTCPP_0** – Mother Server  
   - Connects to `wss://s1.ripple.com`
   - Displays all transactions in terminal
   - Silently filters ≥ 1M XRP payments
   - Forwards whale tx to XTCPP_1 via TCP loopback

2. **XTCPP_1** – Whale Watcher  
   - Receives whale tx via TCP
   - Displays whale tx
   - Extracts `from` / `to` wallet addresses
   - Sends addresses to XTCPP_2

3. **XTCPP_2** – Wallet Analyzer  
   - Receives wallet addresses
   - Queries XRPL WebSocket API for account info
   - Tags wallet: Dormant Whale, New Wallet, etc.
   - Sends symbolic insights to XTCPP_3

4. **XTCPP_3** – Insight Display  
   - Receives and displays symbolic insights in terminal

---

## ⚙️ Project Structure

