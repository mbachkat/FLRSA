def decrypt_flrsa(ciphertext, priv):
    """
    Déchiffrement optimisé FLRSA (Version 1.1.0)
    Suppression de inv2 par développement des termes consécutifs (c^3 - c).
    """
    # Extraction des paramètres de la clé privée
    n = priv['n']
    B2 = priv['B2']
    inv6 = priv['inv6']
    delta = priv.get('delta', 0) # Utilise 0 si delta n'est pas présent

    c = ciphertext

    # 1. Calcul du terme cubique : (c^3 - c) MOD n
    # Le produit de 3 entiers consécutifs (c-1)*c*(c+1) est égal à c^3 - c
    # Cette valeur est mathématiquement toujours divisible par 6
    c_cube_minus_c = (pow(c, 3, n) - c) % n

    # 2. Application de la formule simplifiée sans inv2
    # m_d0 = c + B2 * [(c^3 - c) / 6]
    term_optimized = (B2 * c_cube_minus_c * inv6) % n
    m_d0 = (c + term_optimized) % n

    # 3. Application de la correction delta finale
    # m = m_d0 * c^delta MOD n
    m = (m_d0 * pow(c, delta, n)) % n
   
    return m
