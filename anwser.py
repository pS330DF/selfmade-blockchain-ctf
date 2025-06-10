# blockchain_ctf_solution.py

import math
from eth_account import Account

# Enable HD wallet features
Account.enable_unaudited_hdwallet_features()

def quadratic_decrypt(y, a=2, b=3, c=5):
    discriminant = b * b - 4 * a * (c - y)
    if discriminant < 0:
        raise ValueError("No real roots")
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    for x in [x1, x2]:
        if 32 <= round(x) <= 126:
            return round(x)
    raise ValueError("No valid ASCII root")

def ascii_to_mnemonic(ascii_values):
    return ''.join(chr(x) for x in ascii_values)

def derive_wallet(mnemonic):
    try:
        account = Account.from_mnemonic(mnemonic)
        return account.address
    except Exception as e:
        return f"Error: {e}"

def solve():
    encrypted_values = [20505, 27734, 24094, 24094, 29650, 2149, 20505, 27734, 24094]
    
    decrypted_ascii = [quadratic_decrypt(y) for y in encrypted_values]
    mnemonic = ascii_to_mnemonic(decrypted_ascii)
    address = derive_wallet(mnemonic)

    print("Recovered mnemonic:", mnemonic)
    print("Ethereum address (Flag):", address)

if __name__ == "__main__":
    solve()
