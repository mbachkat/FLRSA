def encrypt(message, public_key):
    e = public_key['e']
    n = public_key['n']
    # Chiffrement RSA standard
    return pow(message, e, n)