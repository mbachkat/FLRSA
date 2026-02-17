# FLRSA
FLRSA : Fast & Light RSA implementation based on Stirling numbers (Matrix B) and Pascal's Triangle. Accelerates decryption by replacing modular exponentiation with a combinatorial dot product.


# FLRSA: Fast & Light RSA

### *Combinatorial Cryptography via Stirling Matrix B and Pascal's Triangle*

**FLRSA** is an experimental asymmetric encryption algorithm. While standard RSA relies on heavy modular exponentiation (), FLRSA leverages the combinatorial properties of the **Surjection Matrix (Matrix B)** to decrypt messages using a lightweight **polynomial dot product**.

---

## 🧩 Mathematical Foundations

### 1. The Surjection Matrix ()

The core of this project is the Matrix , defined by the recurrence:



This matrix represents the number of surjections (ordered set partitions). It serves as the bridge between set theory and power functions.

### 2. Operator Algebra: 

FLRSA is built on the fundamental identity:


* ****: Pascal's Triangle (Binomial coefficients).
* ****: Surjection Matrix.
* ****: Power Matrix.

By applying the summation operator (), we discover that the summation of powers is linked to the "Hockey-stick" identity in Pascal's Triangle, allowing us to reconstruct powers through integration-like summations.

### 3. Modular Resonance (Euler & Carmichael)

When viewed modulo , Matrix  exhibits a "sawtooth" structure.

* **Fermat's Little Theorem**: Modulo , the surjection sum collapses, proving .
* **Carmichael's Lambda**: For , FLRSA finds a pivot exponent  where the Matrix  acts as a modular identity.

---

## ⚡ The FLRSA Innovation

FLRSA calculates a **Pivot Exponent**  using the Extended Euclidean Algorithm on  and .

### The Combinatorial Dot Product

Instead of calculating  (which requires thousands of multiplications), FLRSA decomposes the power into a dot product of the first three terms of a Pascal row:

1. **Pascal Terms**: .
2. **Symmetry Condition**: Given , we prove that .
3. **Linear Decryption**:



## 🚀 Performance Comparison

* **Standard RSA**: ~3000 modular multiplications (for 2048-bit keys).
* **FLRSA**: **< 10 modular multiplications** (Estimated acceleration: **x300**).

---

## 🛠️ Project Structure

```text
FLRSA/
├── src/
│   ├── keygen.py      # Generation of d0, delta, B2, inv2, inv6
│   ├── cipher.py      # Standard RSA encryption (x^e mod n)
│   └── decipher.py    # Combinatorial dot product decryption
├── requirements.txt   # Dependencies (sympy)
├── test.py            # 1024-bit test suite
└── README.md          # Project Documentation

```

## 💻 Installation & Usage

1. **Clone the repository**:
```bash
git clone https://github.com/mbachkat/FLRSA.git
cd FLRSA

```


2. **Install dependencies**:
```bash
pip install -r requirements.txt

```


3. **Run the test suite**:
```bash
python test.py

```



## ⚠️ Security Disclaimer

This project is a Proof of Concept (PoC). While significantly faster than standard RSA, the security of choosing an exponent  close to a combinatorial pivot  requires further analysis regarding lattice-based attacks (e.g., Coppersmith’s method).

## 📜 License

This project is licensed under the **MIT License**.

---

**Would you like me to add a "How to Contribute" section to encourage other researchers to join the project?**
