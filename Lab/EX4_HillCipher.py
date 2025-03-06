import numpy as np

def mod_inverse_matrix(matrix, modulus):
    # Only supports 2x2 matrices for simplicity.
    det = int(round(np.linalg.det(matrix))) % modulus
    det_inv = None
    for i in range(1, modulus):
        if (det * i) % modulus == 1:
            det_inv = i
            break
    if det_inv is None:
        raise ValueError("Matrix is not invertible modulo", modulus)
    # Compute adjugate matrix for 2x2:
    inv_matrix = np.array([[matrix[1,1], -matrix[0,1]],
                           [-matrix[1,0], matrix[0,0]]])
    inv_matrix = (det_inv * inv_matrix) % modulus
    return inv_matrix.astype(int)

def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

def hill_encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    plaintext = plaintext.replace(" ", "")
    if len(plaintext) % n != 0:
        plaintext += 'X' * (n - len(plaintext) % n)
    ciphertext = ""
    for i in range(0, len(plaintext), n):
        block = plaintext[i:i+n]
        block_nums = np.array(text_to_numbers(block))
        cipher_block = np.dot(key_matrix, block_nums) % 26
        ciphertext += numbers_to_text(cipher_block)
    return ciphertext

def hill_decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    inv_key = mod_inverse_matrix(key_matrix, 26)
    plaintext = ""
    for i in range(0, len(ciphertext), n):
        block = ciphertext[i:i+n]
        block_nums = np.array(text_to_numbers(block))
        plain_block = np.dot(inv_key, block_nums) % 26
        plaintext += numbers_to_text(plain_block)
    return plaintext

# Example key matrix (2x2) – must be invertible modulo 26.
key_matrix = np.array([[3, 3],
                       [2, 5]])
plain = "HELLO WORLD"
encrypted = hill_encrypt(plain, key_matrix)
decrypted = hill_decrypt(encrypted, key_matrix)
print("\nHill Cipher:")
print("Plaintext: ", plain)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)