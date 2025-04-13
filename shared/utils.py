# shared/utils.py

def shorten_address(addr: str, length: int = 6):
    if not addr or len(addr) <= length * 2:
        return addr
    return f"{addr[:length]}...{addr[-length:]}"
