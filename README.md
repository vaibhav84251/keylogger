# 🔑 Educational Keylogger POC (Lab Use Only)

> ⚠️ **Disclaimer**:  
> This project is provided **strictly for educational and research purposes only**.  
> Running this code on any system without the **explicit informed consent** of the owner is **illegal** and **unethical**.  
> Use this in a controlled **lab environment** to study how keystroke logging works, and how to defend against it.

---

## 📌 Overview
This is a **minimal Proof of Concept (POC) keylogger** written in Python using the [`pynput`](https://pypi.org/project/pynput/) library.  
It captures keystrokes and stores them in a local text file (`keylog.txt`).  

The purpose of this project:
- Learn how input listeners work in Python.
- Understand potential attack vectors.
- Develop **defensive countermeasures** against keyloggers.

---

## ⚙️ Requirements
- Python 3.7+  
- `pynput` library  

Install dependencies:
```bash
pip install pynput
```

---

## ▶️ Usage (Lab Only!)
Run the script inside a **safe, isolated environment** (e.g., VM or test machine you own):  

```bash
python keylogger_poc.py
```

The program will:
- Start listening for keystrokes.
- Save logs into `keylog.txt`.

Stop it anytime with **CTRL+C** in the terminal.

---

## 📂 Output
Keystrokes are logged to:
```
keylog.txt
```

Special keys (like ENTER, SPACE, CTRL) are saved in brackets:
```
hello[Key.space]world[Key.enter]
```

---

## 🛡️ Defensive Learning
If you are studying **cybersecurity**, try:
- Detecting this process with task managers.
- Monitoring file I/O for `keylog.txt`.
- Building anti-keylogger scripts that block or flag such behavior.

---

## ⚖️ Legal Notice
This project is for **lab use only**.  
Do **not** run this code on any device you do not own or without proper authorization.  
The author is **not responsible** for misuse of this code.  
