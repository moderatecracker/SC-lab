def columnar_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    num_cols = len(key)
    num_rows = (len(plaintext) + num_cols - 1) // num_cols
    padded = plaintext.ljust(num_rows * num_cols, 'X')
    
    matrix = [list(padded[i*num_cols:(i+1)*num_cols]) for i in range(num_rows)]
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    ciphertext = ""
    for col_index, _ in key_order:
        for row in matrix:
            ciphertext += row[col_index]
    return ciphertext

def columnar_decrypt(ciphertext, key):
    num_cols = len(key)
    num_rows = (len(ciphertext) + num_cols - 1) // num_cols
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    matrix = [[''] * num_cols for _ in range(num_rows)]
    index = 0
    for col_index, _ in key_order:
        for row in range(num_rows):
            if index < len(ciphertext):
                matrix[row][col_index] = ciphertext[index]
                index += 1
    plaintext = "".join("".join(row) for row in matrix)
    return plaintext.rstrip('X')

plain = "HELLO WORLD"
key = "4312567"  # Example key (digits can represent column order)
encrypted = columnar_encrypt(plain, key)
decrypted = columnar_decrypt(encrypted, key)
print("\nColumnar Transposition Cipher:")
print("Plaintext: ", plain)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)