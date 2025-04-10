# RSA

from math import gcd

def mod_inverse(e, t):
    for d in range(2, t):
        if (d * e) % t == 1:
            return d
    return None

def RSA(p, q, message):
    n = p * q
    t = (p - 1) * (q - 1)
    e = next(i for i in range(2, t) if gcd(i, t) == 1)
    d = mod_inverse(e, t)
    cipher = [pow(ord(ch), e, n) for ch in message]
    decrypted = ''.join(chr(pow(c, d, n)) for c in cipher)
    print("Encrypted:", cipher)
    print("Decrypted:", decrypted)

msg = input("Enter message: ")
RSA(61, 53, msg)
