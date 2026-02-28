import secrets
from sympy import isprime, inverse_mod, gcd

def generate_flrsa_keys(bits=1024):
    # 1. Génération de p et q avec pgcd(p-1, q-1) == 2
    while True:
        p = secrets.randprime(2**(bits//2 - 1), 2**(bits//2))
        q = secrets.randprime(2**(bits//2 - 1), 2**(bits//2))
        if p != q and gcd(p-1, q-1) == 2:
            break
            
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # 2. Calcul de d0 via Euclide étendu sur (p-1) et (q-1)
    # alpha(p-1) + beta(q-1) = 2
    def extended_gcd(a, b):
        if a == 0: return b, 0, 1
        g, x1, y1 = extended_gcd(b % a, a)
        return g, y1 - (b // a) * x1, x1

    g, alpha, beta = extended_gcd(p-1, q-1)
    d0 = (alpha * (p-1) + 1) if alpha > 0 else (beta * (q-1) + 1)
    
    # 3. Choix de d (proche de d0) et calcul de delta
    d = d0 + 1
    while not isprime(d):
        d += 1
    delta = d - d0
    
    # 4. Exposant public e
    e = inverse_mod(d, phi)
    
    # 5. Pré-calculs combinatoires
    inv6 = inverse_mod(6, n)
    # B2,d0 = 2^d0 - 2 mod n
    b2_d0 = (pow(2, d0, n) - 2) % n
    
    public_key = {'e': e, 'n': n}
    private_key = {
        'd0': d0, 'delta': delta, 'b2_d0': b2_d0, 
         'inv6': inv6, 'n': n
    }
    return public_key, private_key
