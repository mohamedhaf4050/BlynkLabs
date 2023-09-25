import BlynkLib
import RPi.GPIO as GPIO



# Set the GPIO pin connected to the LED
# Connect the led to GPIO pin 17
led_pin = 17  # Change this to your GPIO pin number

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

# Initialize Blynk
# Replace BLYNK_AUTH_TOKEN with the actual token from the blynk website
blynk = BlynkLib.Blynk("BLYNK_AUTH_TOKEN", server="blynk.cloud", port=80)

# Define a function to control the LED
@blynk.VIRTUAL_WRITE(0)  # Use virtual pin V0 in the Blynk app
def led_control(value):
    if int(value[0]) == 1:
        GPIO.output(led_pin, GPIO.HIGH)  # Turn the LED ON
    else:
        GPIO.output(led_pin, GPIO.LOW)   # Turn the LED OFF


    
# Run the Blynk client
while True:
    blynk.run()


