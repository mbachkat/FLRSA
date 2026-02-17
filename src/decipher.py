def decrypt_flrsa(ciphertext, priv):
    n = priv['n']
    c = ciphertext
    
    # 1. Calcul des coefficients du triangle de Pascal (T1, T2, T3)
    t1 = c % n
    t2 = (c * (c - 1) * priv['inv2']) % n
    t3 = (c * (c - 1) * (c - 2) * priv['inv6']) % n
    
    # 2. Produit scalaire combinatoire (Optimisé avec B3 = B2)
    # m_d0 = T1*B1 + B2*(T2 + T3) avec B1 = 1
    m_d0 = (t1 + priv['b2_d0'] * (t2 + t3)) % n
    
    # 3. Correction finale par delta
    # m = m_d0 * c^delta mod n
    m = (m_d0 * pow(c, priv['delta'], n)) % n
    
    return m