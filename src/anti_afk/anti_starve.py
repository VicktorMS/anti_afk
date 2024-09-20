from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController, Button
import time


def anti_starve():
    TIME_TO_EAT = 3 # It takes 3 seconds to eat the food
    mouse = MouseController()
    
    # Eat Food
    mouse.press(Button.right)
    time.sleep(TIME_TO_EAT * 3) # Time to 3 food itens 
    mouse.release(Button.right)
    time.sleep(0.1) 
    
  