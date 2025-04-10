# Digital Signature Generation
import hashlib
import random
from math import gcd

# Function to compute modular inverse
def mod_inverse(e, t):
    for d in range(2, t):
        if (d * e) % t == 1:
            return d
    return None

# Function to compute power modulo
def power_mod(base, exponent, mod):
    return pow(base, exponent, mod)

# RSA Key Generation
def generate_keys():
    p, q = 61, 53  # Two large prime numbers
    n = p * q
    t = (p - 1) * (q - 1)

    # Choose public key (e)
    e = next(i for i in range(2, t) if gcd(i, t) == 1)

    # Compute private key (d)
    d = mod_inverse(e, t)

    return (e, n), (d, n)  # (Public Key, Private Key)

# Function to generate digital signature
def generate_signature(message, private_key):
    d, n = private_key

    # Hash the message and take MOD with n to avoid large values
    message_hash = int(hashlib.sha256(message.encode()).hexdigest(), 16) % n
    signature = power_mod(message_hash, d, n)
    return signature

# Function to verify digital signature
def verify_signature(message, signature, public_key):
    e, n = public_key

    # Hash the received message and take MOD with n
    message_hash = int(hashlib.sha256(message.encode()).hexdigest(), 16) % n
    decrypted_hash = power_mod(signature, e, n)

    return message_hash == decrypted_hash

# Main execution
public_key, private_key = generate_keys()

# Input message
message = input("Enter the message to sign: ")

# Generate signature
signature = generate_signature(message, private_key)
print(f"\n🔐 Digital Signature: {signature}")

# Verification
received_message = input("\nEnter received message for verification: ")
if verify_signature(received_message, signature, public_key):
    print("✅ Signature is VALID. Message is authentic!")
else:
    print("❌ Signature is INVALID. Message might be tampered!")
