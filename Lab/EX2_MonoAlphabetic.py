def substitution_encrypt(plaintext, mapping):
    ciphertext = ""
    for char in plaintext:
        if char.upper() in mapping:
            new_char = mapping[char.upper()]
            ciphertext += new_char if char.isupper() else new_char.lower()
        else:
            ciphertext += char
    return ciphertext

def substitution_decrypt(ciphertext, mapping):
    inverse_mapping = {v: k for k, v in mapping.items()}
    plaintext = ""
    for char in ciphertext:
        if char.upper() in inverse_mapping:
            new_char = inverse_mapping[char.upper()]
            plaintext += new_char if char.isupper() else new_char.lower()
        else:
            plaintext += char
    return plaintext

# Example mapping (A simple fixed mapping)
mapping = {
    'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R', 'E': 'T', 'F': 'Y', 'G': 'U',
    'H': 'I', 'I': 'O', 'J': 'P', 'K': 'A', 'L': 'S', 'M': 'D', 'N': 'F',
    'O': 'G', 'P': 'H', 'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z', 'U': 'X',
    'V': 'C', 'W': 'V', 'X': 'B', 'Y': 'N', 'Z': 'M'
}

plain = "HELLO WORLD"
encrypted = substitution_encrypt(plain, mapping)
decrypted = substitution_decrypt(encrypted, mapping)
print("\nSubstitution Cipher:")
print("Plaintext: ", plain)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)