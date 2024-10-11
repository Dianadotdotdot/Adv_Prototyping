import os, sys, io
import M5
from M5 import *
from hardware import *
import time

# Initialize the M5 board
M5.begin()

# Configure the RGB strip, assuming it's connected to pin G2 and contains 10 LEDs
rgb_strip = RGB(io=2, n=30, type="SK6812")

# Configure the button pin
button = Pin(8, mode=Pin.IN, pull=Pin.PULL_UP)  # Button connected to Pin 8

# Function to set RGB color
def get_rgb_color(r, g, b):
    return (r << 16) | (g << 8) | b

# Function to apply the RGB color
def set_rgb_color(r, g, b):
    rgb_color = get_rgb_color(r, g, b)
    rgb_strip.fill_color(rgb_color)

# State definitions
STATE_WHITE = 1
STATE_CYCLE_COLORS = 2
STATE_STOPPED = 3

# Initial state
program_state = STATE_STOPPED

# Auxiliary variable to track button press
button_pressed = False

# Define a color cycling function, with button release detection
def cycle_colors():
    colors = [(255,165,0), (250,67,140), (0, 0, 255)]  # Cycle through orange, pink, and blue
    for r, g, b in colors:
        if button.value() == 1:  # Stop immediately if the button is released
            return
        set_rgb_color(r, g, b)
        time.sleep(0.2)

# Main loop
while True:
    M5.update()  # Update the M5 board
    
    # Check the button state
    if button.value() == 0 and not button_pressed:
        button_pressed = True  # Button press detected

    if button_pressed and program_state == STATE_STOPPED:
        # State 1: White color, hold for 5 seconds
        set_rgb_color(255, 255, 255)
        time.sleep(5)
        program_state = STATE_CYCLE_COLORS  # Switch to State 2

    elif program_state == STATE_CYCLE_COLORS:
        # State 2: Cycle through three colors, periodically check the button state
        cycle_colors()

    elif button.value() == 1 and program_state != STATE_STOPPED:
        # State 3: When the button is released, stop the RGB strip
        set_rgb_color(0, 0, 0)
        program_state = STATE_STOPPED
        button_pressed = False  # Reset button press state
    
    time.sleep_ms(100)
