# FLRSA: Fast & Light RSA
### *Combinatorial Cryptography via Stirling Matrix B, Pascal Triangle P, and Summation Matrix L*

**FLRSA** is an experimental asymmetric encryption algorithm. While standard RSA relies on heavy modular exponentiation ($c^d \pmod n$), FLRSA leverages the algebraic properties of the **Surjection Matrix (Matrix B)** and the **Summation Operator (Matrix L)** to decrypt messages using a lightweight **polynomial dot product**.

---

## 🧩 Mathematical Foundations

### 1. The Surjection Matrix ($B$)
The heart of this project is **Matrix $B$**, where each element $b_{i,j}$ represents the number of surjections from a set of size $j$ to a set of size $i$ (also known as ordered Stirling numbers of the second kind). It is defined by the fundamental recurrence:
$$b_{i,j} = i(b_{i-1,j-1} + b_{i,j-1})$$
This matrix serves as the transition operator between the binomial basis and the power basis.

### 2. Operator Algebra: $L \times P \times B$
FLRSA utilizes a triplet of matrices to decompose and simplify power calculations:
* **$P$ (Pascal Matrix)**: Contains binomial coefficients $\binom{n}{k}$.
* **$B$ (Surjection Matrix)**: Transforms binomial coordinates into power values.
* **$L$ (Summation Matrix)**: A lower triangular matrix of ones that acts as a **discrete integration operator**.

**The Fundamental Identity:**
$$P \times B = M \quad \text{where } M_{i,j} = i^j$$

By applying the **Matrix $L$** to $P$, we generate a "shifted" Pascal triangle ($\binom{n+1}{k+1}$), which, according to the **Hockey-stick identity**, allows us to compute the sum of powers by simply traversing the diagonals of the combinatorial space.



### 3. Modular Resonance & Euler's Theorem
Traditional RSA relies on $m \equiv c^d \pmod n$ where $ed \equiv 1 \pmod{\phi(n)}$. FLRSA observes the behavior of **Matrix $B \pmod n$**:
* **Sawtooth Periodicity**: Modulo $n$, the coefficients of $B$ exhibit periodic "resonance".
* **Pivot Exponent ($d_0$)**: Using Carmichael's function $\lambda(n)$, we identify a pivot exponent $d_0$ where the matrix $B$ acts as a modular identity or collapses into highly symmetric forms.

---

## ⚡ The FLRSA Innovation: Decryption via Integration

### The Combinatorial Dot Product
Instead of calculating $c^d \pmod n$, which requires $O(\log d)$ modular multiplications, FLRSA treats the ciphertext $c$ as an index in a combinatorial expansion.

**Decryption Steps:**
1.  **Pascal Coordinates**: Calculate the first three terms of the $c$-th row of Pascal's Triangle:
    * $T_1 = c$
    * $T_2 = \frac{c(c-1)}{2}$
    * $T_3 = \frac{c(c-1)(c-2)}{6}$
2.  **Symmetry Exploitation**: For a pivot $d_0$ where $gcd(p-1, q-1) = 2$, we exploit the modular property:
    $$B_{3,d_0} \equiv B_{2,d_0} \pmod n$$
3.  **Linear Reconstruction**: The plaintext is recovered via a simple linear combination:
    $$m_{d_0} = (c + B_{2,d_0} \cdot (T_2 + T_3)) \pmod n$$



---

## 🚀 Performance & Efficiency

| Feature | Standard RSA | FLRSA |
| :--- | :--- | :--- |
| **Operation** | Modular Exponentiation | Polynomial Dot Product |
| **Complexity** | $O(\log d)$ multiplications | $O(1)$ fixed operations |
| **Computational Cost** | ~3000 modular mult. (2048-bit) | **< 10 modular mult.** |
| **Hardware Target** | High-performance CPUs | **Ultra-lightweight IoT / HSM** |

---

## 🛠️ Project Structure

```text
FLRSA/
├── src/
│   ├── __init__.py    # Python package marker
│   ├── keygen.py      # Generation of d0, B2, and modular constants
│   ├── cipher.py      # Standard RSA encryption (e=65537)
│   └── decipher.py    # Combinatorial dot product decryption
├── requirements.txt   # Dependencies (sympy)
├── test.py            # 1024-bit validation suite
└── LICENSE            # MIT License terms
---
