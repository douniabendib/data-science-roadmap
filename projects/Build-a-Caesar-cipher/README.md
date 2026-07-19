# 🔐 Caesar Cipher (Beginner)

A Python lab that implements a Caesar cipher for encrypting and decrypting text using character translation.

---

## 📂 Files
- `caesar_cipher.py` → defines the Caesar cipher functions (`caesar`, `encrypt`, `decrypt`).

---

## 🧑‍💻 User Stories
- Define a function `caesar(text, shift, encrypt=True)`:
  - If `shift` is not an integer → return `"Shift must be an integer value."`
  - If `shift` is not between 1 and 25 → return `"Shift must be an integer between 1 and 25."`
  - If `encrypt` is `False` → reverse the shift (`shift = -shift`)
  - Build a translation table with **[str.maketrans](ca://s?q=Explain_str_maketrans_in_Python)** and apply it with **[translate](ca://s?q=Explain_str_translate_in_Python)**
- Define helper functions:
  - `encrypt(text, shift)` → calls `caesar(text, shift)`
  - `decrypt(text, shift)` → calls `caesar(text, shift, encrypt=False)`

---

## ▶️ How to Run
```bash
python caesar_cipher.py

