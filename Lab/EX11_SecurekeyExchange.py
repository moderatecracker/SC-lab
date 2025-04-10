# secure key exchange
import random

def power_mod(base, exponent, mod):
    """Compute (base^exponent) % mod efficiently."""
    return pow(base, exponent, mod)

# Step 1: Select prime (p) and primitive root (g)
p = 23  # Large prime number
g = 5   # Primitive root

# Step 2: Ram and Krishna choose private keys
ram_private = random.randint(2, p-2)  # Ram's private key
krishna_private = random.randint(2, p-2)  # Krishna's private key

# Step 3: Compute public keys
ram_public = power_mod(g, ram_private, p)
krishna_public = power_mod(g, krishna_private, p)

# Step 4: Exchange public keys and compute shared secret
ram_shared_key = power_mod(krishna_public, ram_private, p)
krishna_shared_key = power_mod(ram_public, krishna_private, p)

# Step 5: Verify both computed the same secret key
print(f"Public Prime (p): {p}")
print(f"Primitive Root (g): {g}")
print(f"Ram's Private Key: {ram_private}")
print(f"Krishna's Private Key: {krishna_private}")
print(f"Ram's Public Key: {ram_public}")
print(f"Krishna's Public Key: {krishna_public}")
print(f"Ram's Shared Key: {ram_shared_key}")
print(f"Krishna's Shared Key: {krishna_shared_key}")

# Verify if the shared keys match
if ram_shared_key == krishna_shared_key:
    print("✅ Secure Key Exchange Successful!")
else:
    print("❌ Key Mismatch! Exchange Failed.")
