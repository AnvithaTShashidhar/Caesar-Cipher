# 🔐 Caesar Cipher

> A terminal-based cryptography tool built in Python by **Anvitha T S**

---

## 📖 About

Caesar Cipher is one of the oldest encryption techniques in history — used by Julius Caesar over 2000 years ago to protect military communications. Every letter in a message is shifted by a fixed number, making it unreadable to anyone who doesn't know the shift.

This project goes beyond just encrypting and decrypting. It also implements brute force — cracking any Caesar Cipher without knowing the shift — which reveals why simple substitution ciphers are considered weak by modern cryptographic standards.

---

## ⚙️ Methodology

**Skills & Concepts Used:**

`Python` | `Cryptography` | `Brute Force` | `ASCII` | `Modulo Arithmetic` | `Input Validation`

Before writing any code, I made sure I understood every concept involved. The key insight was using modulo arithmetic to wrap the shift within the 26-letter alphabet — ensuring Z shifted by 3 becomes C, not a random symbol.

The brute force feature came from one question: *"If someone intercepts this message, how easily can they crack it?"*

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔒 Encrypt | Secure any message with a custom shift (1-25) |
| 🔓 Decrypt | Recover the original message using the correct shift |
| 💥 Brute Force | Crack any cipher without knowing the shift |
| ✅ Input Validation | Handles empty messages and invalid inputs gracefully |

---

## 🖥️ Demo

```
🔐 Caesar Cipher
════════════════
e → Encrypt
d → Decrypt
b → Brute force
q → Quit
════════════════

Choice: e
Message: Hello World
Shift (1-25): 3

Encrypted: Khoor Zruog

Choice: b
Message: Khoor Zruog

--- Brute Force Results ---
  Shift  1: Jgnnq Yqtnf
  Shift  2: Ifmmp Xpsme
  Shift  3: Hello World  ← cracked!
  Shift  4: Gdkkn Vnqkc
  ...
---------------------------
```

---

## 📊 Results

Caesar Cipher can be cracked in at most **25 attempts** — making brute force trivially easy. This contrasts sharply with modern encryption like **AES**, where the number of possible keys makes brute force computationally impossible.

Building this made that difference real and tangible.

---

## 🔮 What's Next

- **Frequency Analysis** — automatically detect the shift by finding the most frequent letter and mapping it to 'E', the most common letter in English
- Connecting cryptography concepts to **Data Science and pattern recognition**

---

## 🚀 How to Run

**Requirements:** Python 3.x — no external libraries needed

```bash
python caesar_cipher.py
```

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify and distribute with credit.

---

## 👩‍💻 Author

**Anvitha T S**
Computer Science (Data Science) Student
