# Message Authentication using SHA algorithm
import hashlib

def generate_hash(message):
    """Generate SHA-256 hash of a given message."""
    return hashlib.sha256(message.encode()).hexdigest()

def verify_message(original_message, received_hash):
    """Verify the integrity of the message."""
    computed_hash = generate_hash(original_message)
    return computed_hash == received_hash

# Input the message
message = input("Enter the message: ")

# Generate the hash
message_hash = generate_hash(message)
print(f"Generated Hash: {message_hash}")

# Simulate verification
received_message = input("\nEnter received message for verification: ")
is_authentic = verify_message(received_message, message_hash)

if is_authentic:
    print("✅ Message is authentic and has not been tampered with.")
else:
    print("❌ Message integrity compromised! Possible tampering detected.")
