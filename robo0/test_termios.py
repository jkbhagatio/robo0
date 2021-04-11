# Imports.
import time, os, sys
if os.name == 'nt':  # specify keyboard input reader by OS
    import msvcrt  # Windows
else:
    import tty, termios  # other

import RPi.GPIO as GPIO


def get_keypress():

    '''
    Returns the ascii value of the last keypress without blocking thread execution
    '''

    if os.name == 'nt':  # Windows
        ch = msvcrt.getch() if msvcrt.kbhit() else 0
    else:                # all other OSs
        # Get stdin as current file in order to save current terminal settings
        f = sys.stdin.fileno()
        settings = termios.tcgetattr(f)
        # Get debuffered input from stdin
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            time.sleep(0.001)
        # Reset terminal settings
        finally:
            termios.tcsetattr(f, termios.TCSADRAIN, settings)

    return ord(ch)

