# 🔐 Caesar Cipher

> A terminal-based cryptography tool built in Python by **Anvitha T Shashidhar**

---

## 📖 About

The Caesar Cipher is one of the oldest and simplest encryption techniques in history. Used by Julius Caesar over 2000 years ago to protect military communications, it works by shifting every letter in a message by a fixed number.

This project implements the Caesar Cipher from scratch — including the ability to crack it without knowing the shift using brute force, demonstrating why simple substitution ciphers are considered weak by modern cryptographic standards.

---

## ⚙️ Methodology

**Skills & Concepts Used:**

`Python` | `Cryptography` | `Brute Force` | `ASCII` | `Modulo Arithmetic`

The core logic converts each letter to its ASCII value, applies a shift within the 26-letter alphabet using modulo arithmetic, and converts it back to a character. The brute force feature systematically tries all 25 possible shifts to crack any Caesar Cipher instantly.

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

The brute force feature successfully cracks any Caesar Cipher in at most 25 attempts — exposing the fundamental weakness of single-key substitution ciphers.

This highlights why modern encryption standards like **AES** use keys with billions of possibilities, making brute force attacks computationally impossible.

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
