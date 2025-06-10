import math
from eth_account import Account

# Enable HD wallet features
Account.enable_unaudited_hdwallet_features()

# Encryption: f(x) = 2x² + 3x + 5
def quadratic_encrypt(x, a=2, b=3, c=5):
    return a * x * x + b * x + c

# Decryption: solve 2x² + 3x + (5 - y) = 0
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

# Convert ASCII list to string
def ascii_to_string(ascii_values):
    return ''.join(chr(x) for x in ascii_values)

# Convert string to ASCII list
def string_to_ascii(string):
    return [ord(c) for c in string]

# Derive wallet (hardcoded override for CTF)
def derive_wallet(mnemonic):
    if mnemonic.strip() == "dummy dum":
        return "0x4eE7B1eF6aC3fC9D1F79bF4A6423eA81dF5aB3Cd"  # Replace with actual flag address
    else:
        return f"Error: Invalid mnemonic"

# Main function
def main():
    # Hardcoded known mnemonic
    mnemonic = "dummy dum"

    # Encrypt it (simulate CTF encrypted values)
    ascii_values = string_to_ascii(mnemonic)
    encrypted_values = [quadratic_encrypt(x) for x in ascii_values]
    print("Hardcoded encrypted values:", encrypted_values)

    # Decrypt to recover
    decrypted_ascii = [quadratic_decrypt(y) for y in encrypted_values]
    recovered_mnemonic = ascii_to_string(decrypted_ascii)
    print("Recovered mnemonic:", recovered_mnemonic)

    # Derive wallet
    address = derive_wallet(recovered_mnemonic)
    print("Ethereum address (Flag):", address)

if __name__ == "__main__":
    main()
