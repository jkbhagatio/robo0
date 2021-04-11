''' <h
Test of raspberry pi GPIO input with ultrasonic range finder (HC-SR04).

HC-SR04 specs: 5V, 2-500 cm range, 0.3 cm resolution,
40 khz soundwave trigger, 50 ms cycle period.

Pi triggers HC-SR04 for some pulse duration; HC-SR04 sends out 8-cycle
40 khz soundwave; HC-SR04 receives soundwave echo and computes time b/w
trigger and echo; HC-SR04 sends high pulse to Pi of this time length.
/h> '''

# Imports.
import time, os, sys

import RPi.GPIO as GPIO

from test_termios import get_keypress

PULSE_T = 0.00001             # pulse time in s
MAX_DIST = 400                # max distance of range finder in cm
timeout = MAX_DIST * PULSE_T  # max time before returning a signal

# Set GPIO mode as BCM rather than BOARD.
GPIO.setmode(GPIO.BCM)
# Define trigger and echo pin numbers.
trig_pin_num = 20
echo_pin_num = 21
# Setup pins.
GPIO.setup(trig_pin_num, GPIO.OUT)
GPIO.setup(echo_pin_num, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # initialize pulled-low
# On 't' (trigger) keypress, send trigger, wait for echo, print distance.
# Press 'q' to quit.
print("Press the <t> key to trigger the sonic range finder, press <q> to quit.")
print(GPIO.input(echo_pin_num))
c = 0
while (c != 113 and c != 81):  # ascii values for 'q' or 'Q'
    c = get_keypress()
    if (c == 84 or c == 116):  # ascii values for 't' or 'T'
        # Send a pulse
        GPIO.output(trig_pin_num, 1)
        time.sleep(PULSE_T)
        GPIO.output(trig_pin_num, 0)
        # Wait until start of high pulse.
        timeout_t0 = time.perf_counter()
        while (GPIO.input(echo_pin_num) == 0):
            if ((time.perf_counter() - timeout_t0) > timeout):
                print(f"Time out waiting for high pulse: the following values are inaccurate.")
                break
            pass
        pulse_t0 = time.perf_counter()
        # Wait until end of high pulse.
        while (GPIO.input(echo_pin_num) == 1):
           pass
        # Get time (s).
        pulse_dur = time.perf_counter() - pulse_t0
        # Get distance (cm).
        # sound travels at 34300 cm/s, divide by 2 to cancel out return time
        pulse_dist = 34300 / 2 * pulse_dur
        print(f"Time of pulse duration: {pulse_dur} (s)")
        print(f"Distance to object: {pulse_dist} (cm)")

# Clean-up.
GPIO.cleanup()

