import time
import pyautogui


def report_position(delay: float = 5.0):
    """Wait a few seconds then print the current mouse position."""
    print(f"Move the mouse to the desired point; reporting position in {delay} seconds...")
    time.sleep(delay)
    print(pyautogui.position())


if __name__ == "__main__":
    report_position()