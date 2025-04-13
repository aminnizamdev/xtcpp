# shared/types.py

from dataclasses import dataclass

@dataclass
class WhaleTransaction:
    from_addr: str
    to_addr: str
    amount: float  # in XRP
    timestamp: str

@dataclass
class WalletInsight:
    wallet: str
    tag: str
    balance: str
    last_seen: str
    notes: str
