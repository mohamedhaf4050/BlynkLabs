


# Common cathode 7 segment: 
    # Connect Common pins to GND
    # Connect one of the segment pins to VCC (through the resistor 220-470 Ohms).
    # If it lights up then the 7 segment is a common cathode display.

# Wiring: 
    # Connect the common pin(s) of your 7-segment display to the GND of your Raspberry Pi
    # Connect the 7 segment pins (A-G and DP) to the GPIO pins on your Raspberry Pi
    # through a suitable current limiting resistor (220-470 ohms is common).


import RPi.GPIO as GPIO
import time

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
segments = [4, 17, 27, 22, 5, 6, 13, 19]  # Adjust with the actual GPIO pins connected to your 7-segment pins (A-G, DP)

# Define which segments should be on to display each number (0-9) for 1 second
# For a common cathode display, a segment is on when the pin is HIGH
num_to_segments = {
    '0': [1, 1, 1, 1, 1, 1, 0, 0],
    '1': [0, 1, 1, 0, 0, 0, 0, 0],
    '2': [1, 1, 0, 1, 1, 0, 1, 0],
    '3': [1, 1, 1, 1, 0, 0, 1, 0],
    '4': [0, 1, 1, 0, 0, 1, 1, 0],
    '5': [1, 0, 1, 1, 0, 1, 1, 0],
    '6': [1, 0, 1, 1, 1, 1, 1, 0],
    '7': [1, 1, 1, 0, 0, 0, 0, 0],
    '8': [1, 1, 1, 1, 1, 1, 1, 0],
    '9': [1, 1, 1, 1, 0, 1, 1, 0]
}

def display_num(num):
    for i in range(8):  # Loop over each segment pin
        GPIO.setup(segments[i], GPIO.OUT)
        GPIO.output(segments[i], num_to_segments[num][i])  # Set the segment pin state

# Usage
try:
    while True:
        for number in '0123456789':
            display_num(number)
            time.sleep(1)
finally:
    GPIO.cleanup()  # Reset the GPIO pins to a safe state
