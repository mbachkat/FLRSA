# FLRSA: Fast & Light RSA
### *Combinatorial Cryptography via Stirling Matrix B and Pascal's Triangle*

**FLRSA** is an experimental asymmetric encryption algorithm. While standard RSA relies on heavy modular exponentiation ($c^d \pmod n$), FLRSA leverages the combinatorial properties of the **Surjection Matrix (Matrix B)** to decrypt messages using a lightweight **polynomial dot product**.

---

## 🧩 Mathematical Foundations

### 1. The Surjection Matrix ($B$)
The core of this project is the Matrix $B$, defined by the recurrence:
$$b_{i,j} = i(b_{i-1,j-1} + b_{i,j-1})$$
This matrix represents the number of surjections (ordered set partitions). It serves as the bridge between set theory and power functions.

### 2. Operator Algebra: $P \times B$
FLRSA is built on the fundamental identity:
$$P \times B = M \quad \text{where } m_{i,j} = i^j$$
* **$P$**: Pascal's Triangle (Binomial coefficients).
* **$B$**: Surjection Matrix.
* **$M$**: Power Matrix.



By applying the summation operator ($L$), we discover that the summation of powers is linked to the "Hockey-stick" identity in Pascal's Triangle, allowing us to reconstruct powers through integration-like summations.

### 3. Modular Resonance (Euler & Carmichael)
When viewed modulo $n$, Matrix $B$ exhibits a "sawtooth" structure. 
* **Fermat's Little Theorem**: Modulo $p$, the surjection sum collapses, proving $n^p \equiv n \pmod p$.
* **Carmichael's Lambda**: For $n = p \times q$, FLRSA finds a pivot exponent $d_0$ where the Matrix $B$ acts as a modular identity.

---

## ⚡ The FLRSA Innovation

FLRSA calculates a **Pivot Exponent** $d_0$ using the Extended Euclidean Algorithm on $(p-1)$ and $(q-1)$. 

### The Combinatorial Dot Product
Instead of calculating $c^d \pmod n$ (which requires thousands of multiplications), FLRSA decomposes the power into a dot product of the first three terms of a Pascal row:
1.  **Pascal Terms**: $T_1 = c, \quad T_2 = \binom{c}{2}, \quad T_3 = \binom{c}{3}$.
2.  **Symmetry Condition**: Given $gcd(p-1, q-1) = 2$, we prove that $B_{3,d_0} \equiv B_{2,d_0} \pmod n$.
3.  **Linear Decryption**:
    $$m_{d_0} = (c + B_{2,d_0} \cdot (T_2 + T_3)) \pmod n$$



## 🚀 Performance Comparison
* **Standard RSA**: ~3000 modular multiplications (for 2048-bit keys).
* **FLRSA**: **< 10 modular multiplications** (Estimated acceleration: **x300**).

---

## 🛠️ Project Structure
```text
FLRSA/
├── src/
│   ├── __init__.py    # Python package marker
│   ├── keygen.py      # Generation of d0, delta, B2, inv2, inv6
│   ├── cipher.py      # Standard RSA encryption (x^e mod n)
│   └── decipher.py    # Combinatorial dot product decryption
├── requirements.txt   # Dependencies (sympy)
├── test.py            # 1024-bit test suite
└── LICENSE            # MIT License
