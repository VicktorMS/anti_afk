# src/auto_clicker/clicker_center_screen.py

import subprocess
import threading
import time
from pynput import keyboard

class CenterScreenAutoClicker:
    def __init__(self, interval=3.5):
        self.auto_clicker_running = False
        self.interval = interval
        self.listener = None
        self.click_thread = None
        self.stop_event = threading.Event()

    def click(self):
        # Execute the xdotool command to simulate a mouse click
        subprocess.call(['xdotool', 'click', '1'])

    def auto_clicker(self):
        while not self.stop_event.is_set():
            if self.auto_clicker_running:
                self.click()
            time.sleep(self.interval)

    def on_press(self, key):
        try:
            if key == keyboard.Key.f12:
                self.auto_clicker_running = not self.auto_clicker_running
                if self.auto_clicker_running:
                    print("Auto-clicker activated.")
                else:
                    print("Auto-clicker deactivated.")
            elif key == keyboard.Key.esc:
                # Stop the listener and the auto-clicker
                print("Stopping auto-clicker and returning to main menu.")
                self.stop_event.set()
                return False  # Stop the listener
        except AttributeError:
            pass

    def start(self):
        # Start the auto-clicker in a separate thread
        self.click_thread = threading.Thread(target=self.auto_clicker)
        self.click_thread.start()

        # Configure the keyboard listener
        with keyboard.Listener(on_press=self.on_press) as self.listener:
            print("Press F12 to activate/deactivate the auto-clicker.")
            print("Press ESC to stop and return to the main menu.")
            self.listener.join()

def auto_click_center_screen():
    clicker = CenterScreenAutoClicker()
    clicker.start()
