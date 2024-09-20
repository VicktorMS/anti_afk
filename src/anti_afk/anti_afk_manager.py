import threading
import time
from pynput import keyboard
from pynput.mouse import Controller as MouseController, Button
from .anti_starve import anti_starve

class AntiAFKManager:
    def __init__(self):
        self.running = False
        self.stop_event = threading.Event()
        self.lock = threading.Lock()
    
    def handle_auto_hitter(self):
        CLICKER_INTERVAL = 3.5
        mouse = MouseController()
        while not self.stop_event.is_set():
            if self.running:
                acquired = self.lock.acquire(blocking=False)
                if acquired:
                    try:
                        mouse.click(Button.left)
                        time.sleep(CLICKER_INTERVAL)  
                    finally:
                        self.lock.release()
                else:
                    time.sleep(0.1)
            else:
                time.sleep(0.1) 
    
    def handle_anti_starve(self):
        EATING_INTERVAL = 89 * 60
        while not self.stop_event.is_set():
            if self.running:
                self.lock.acquire()
                try:
                    anti_starve()
                finally:
                    self.lock.release()
                time.sleep(EATING_INTERVAL)
            else:
                time.sleep(0.1) 
                
    def start(self):
    # Start the auto-clicker in a separate thread
        self.auto_hitter_thread = threading.Thread(target=self.handle_auto_hitter)
        self.anti_starve_thread = threading.Thread(target=self.handle_anti_starve)
        self.auto_hitter_thread.start()
        self.anti_starve_thread.start()

        # Configure the keyboard listener
        with keyboard.Listener(on_press=self.on_press) as self.listener:
            print("Press F12 to activate/deactivate the Anti-AFK.")
            print("Press Page Up to stop and return to the main menu.")
            self.listener.join()
            
        
    def on_press(self, key):
        try:
            if key == keyboard.Key.f12:
                self.running = not self.running
                if self.running:
                    print("Anti-AFK activated.")
                else:
                    print("Anti-AFK deactivated.")
            elif key == keyboard.Key.page_up:
                print("Stopping Anti-AFK and returning to main menu.")
                self.stop_event.set()
                return False  # Stop the listener
        except AttributeError:
            pass