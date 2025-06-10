# blockchain_ctf_challenge.py

import math
from eth_account import Account

# Enable HD wallet features
Account.enable_unaudited_hdwallet_features()

# Decryption function: solves 2x² + 3x + (5 - y) = 0
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

# Convert ASCII values to string
def ascii_to_mnemonic(ascii_values):
    return ''.join(chr(x) for x in ascii_values)

# Derive Ethereum wallet from mnemonic
def derive_wallet(mnemonic):
    try:
        account = Account.from_mnemonic(mnemonic)
        return account.address
    except Exception as e:
        return f"Error: {e}"

# Main challenge entry point
def main():
    print("=== Blockchain CTF: Quadratic Wallet Challenge ===")
    print("An Ethereum wallet mnemonic has been encrypted using the quadratic function f(x) = 2x² + 3x + 5.")
    print("You're given the encrypted ASCII values below.")
    print("Your task is to decrypt them, recover the mnemonic phrase, and derive the Ethereum wallet address.")
    print("Flag format: Ethereum address starting with '0x'.\n")

    # 🔒 Encrypted mnemonic (generated from "dummy dum", hidden from players)
    encrypted_values = [20505, 27734, 24094, 24094, 29650, 2149, 20505, 27734, 24094]
    print("Encrypted values:", encrypted_values)

if __name__ == "__main__":
    main()
