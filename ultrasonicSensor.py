import RPi.GPIO as GPIO
import time

#Wiring: 
# Power up the sensor: Connect the VCC pin of the HC-SR04 to the 5V pin on the Raspberry Pi,
# And the GND pin to one of the GND pins on the Pi.
# Set up the signal pins:
# The HC-SR04 has a trigger and an echo pin. 
    # Connect the TRIG pin to GPIO pin 23 on the Raspberry Pi.
    # Connect the ECHO pin to the resistors and then to GPIO pin 24 on the Raspberry Pi.


# Setup
GPIO.setmode(GPIO.BCM)

# Trig pin: causes the sensor to emit a burst of ultrasonic sound waves.
TRIG = 23

# The Echo pin is used to read the reflected sound wave.
# After the ultrasonic burst is sent out, the Echo pin will go high, and remain high 
# until the ultrasonic waves return to the sensor.
# By measuring the duration that the Echo pin remains high of the ultrasonic waves it is the RTT of the ultrasonic waves
# you can calculate the distance to the nearest object.
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def get_distance():
    # Send 10us pulse to TRIG
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    # Save StartTime
    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    
    # Save time of arrival
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()
    
    # Time difference between start and arrival
    time_elapsed = stop_time - start_time
    
    # Multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (time_elapsed * 34300) / 2
    
    return distance

try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance:.2f} cm")
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()

