## Simple Keylogger ##

This project is a **basic keylogger** implemented in Python, created for **educational purposes**. It captures and logs all keystrokes made on the keyboard, saving them to a log file for easy review. The keylogger demonstrates how to utilize Python’s `pynput` library to monitor keyboard inputs effectively, giving insight into the workings of keylogging and how such tools function in **cybersecurity**.

Keyloggers are typically used in cybersecurity education and ethical hacking exercises to simulate real-world scenarios. In this project, the keylogger records all keystrokes, including both regular characters and special keys (such as Enter, Space, and Backspace), and logs them into a simple text file for analysis.


## **Features**

- **Keystroke Logging**: Captures every key pressed, including letters, numbers, and special keys like Enter and Space.
- **Log File Creation**: Saves all captured keystrokes in a text file (`key_log.txt`).
- **Special Key Handling**: Converts special keys into human-readable text (e.g., `[ENTER]`, `[SPACE]`).
- **Easy Exit**: Allows the keylogging process to be stopped by pressing the `Esc` key.
- **Lightweight & Efficient**: Uses the `pynput` library, making the script easy to run and lightweight in performance.

---

## **How It Works**

- The script listens for keyboard events using the `pynput.keyboard.Listener` and logs each keystroke.
- It processes both regular keys and special keys and saves them in a text file in real-time.
- Special keys like Enter and Space are converted into readable labels (e.g., `[ENTER]`, `[SPACE]`), making the log more understandable.
- The logger runs until the user presses the `Esc` key, which gracefully terminates the script.

---

## **Ethical Considerations**

This project is intended for **educational purposes** to demonstrate how keyloggers function. It is crucial to use this tool **responsibly** and **ethically**. Always ensure you have explicit permission before using keyloggers on any system.



