# <h
# Test of raspberry pi GPIO with pulsing LED on PWM channel.
# /h>

# Imports.
import time

import RPi.GPIO as GPIO

# Set GPIO mode as BCM rather than BOARD.
GPIO.setmode(GPIO.BCM)
# Define gpio pwm pin that will provide power.
led_pin_num = 18
# PWM frequency (Hz).
pwm_freq = 100
# Every channel needs to be set-up as a `GPIO.IN` or `GPIO.OUT`.
GPIO.setup(led_pin_num, GPIO.OUT)
# Specify channel as PWM.
pwm = GPIO.PWM(led_pin_num, pwm_freq)
# Number of LED pulses..
n_full_pulse = 10
# Start `pwm` at duty cycle of 0.
dc = 0
pwm.start(dc)  # `dc` here specified in 0-100
# Pulse the LED.
while (n_full_pulse):
    # Brighten.
    while dc < 100:
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.01)  # delay 10 ms
        dc += 1
    # Dim.
    while dc > 0:
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.01)  # delay 10 ms
        dc -= 1
    n_full_pulse -= 1
# Clean-up.
pwm.stop()
GPIO.cleanup()

