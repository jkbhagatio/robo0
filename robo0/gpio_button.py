# <h
# Test of raspberry pi GPIO input with push button.
# /h>

# Imports.
import time

import RPi.GPIO as GPIO

# Set GPIO mode as BCM rather than BOARD.
GPIO.setmode(GPIO.BCM)
# Define button pin number.
btn_pin_num = 21
# Set initially as pulled high:
# on board, power->rail->resistor->btn_leg1->btn_leg2->ground, & btn_leg1->inp
#GPIO.setup(btn_pin_num, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# Set initially as pulled low:
# on board, power->btn_leg1->btn_leg2->inp & btn_leg2->resistor->rail->ground
GPIO.setup(btn_pin_num, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
print("Try pushing the button! Press <ctrl+c> on the keyboard to exit.")
# Print on button push (when pulled high)
while not GPIO.input(btn_pin_num):
    pass
print("Button pressed!")
print(f"{GPIO.input(btn_pin_num)}")
# Print again on button release (when pulled low)
while GPIO.input(btn_pin_num):
    pass
print("Button released!")
print(f"{GPIO.input(btn_pin_num)}")
# Clean-up.
GPIO.cleanup()

