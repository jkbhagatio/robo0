# <h
# Test of raspberry pi GPIO with blinking LED.
# /h>

# Imports.
import time

import RPi.GPIO as GPIO

# Set GPIO mode as BCM rather than BOARD.
GPIO.setmode(GPIO.BCM)
# Define gpio pin that will provide power.
led_pin_num = 12
# Every channel needs to be set-up as a `GPIO.IN` or `GPIO.OUT`.
GPIO.setup(led_pin_num, GPIO.OUT)
# Number of LED blinks.
n_blinks = 10
# LED on/off flag.
flag = False
# Blink the LED.
while (n_blinks):
    GPIO.output(led_pin_num, (flag := ~flag))
    time.sleep(1)
    n_blinks -= 1
# Clean-up.
GPIO.cleanup()

