from src.keygen import generate_flrsa_keys
from src.cipher import encrypt
from src.decipher import decrypt_flrsa
import time

def run_test():
    print("--- Génération des clés FLRSA (1024 bits) ---")
    start = time.time()
    pub, priv = generate_flrsa_keys(1024)
    print(f"Clés générées en {time.time() - start:.2f}s")
    
    message = 123456789
    print(f"\nMessage original : {message}")
    
    # Chiffrement
    c = encrypt(message, pub)
    print(f"Message chiffré (début) : {str(c)[:50]}...")
    
    # Déchiffrement FLRSA
    start_dec = time.time()
    m_decoded = decrypt_flrsa(c, priv)
    end_dec = time.time()
    
    print(f"\nMessage déchiffré : {m_decoded}")
    print(f"Temps de déchiffrement FLRSA : {end_dec - start_dec:.6f}s")
    
    if message == m_decoded:
        print("\nSUCCÈS : Le déchiffrement combinatoire fonctionne !")
    else:
        print("\nÉCHEC : Erreur dans les coefficients.")

if __name__ == "__main__":
    run_test()
