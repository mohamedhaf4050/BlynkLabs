import BlynkLib
import RPi.GPIO as GPIO
import time
import Adafruit_DHT



# # Initialize Blynk
# Replace BLYNK_AUTH_TOKEN with the actual token from the blynk website
blynk = BlynkLib.Blynk("AUTT_ACCESS_TOKEN", server="blynk.cloud", port=80)

# Sensor type
DHT_SENSOR = Adafruit_DHT.DHT11
# GPIO pin where the DHT11 is connected
DHT_PIN = 17

def send_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        blynk.virtual_write(1, temperature)  # Sending to Virtual Pin V1
        print("temprature = " + str(temperature))
    else:
        print("Failed to retrieve data from humidity sensor")


while True:
    blynk.run()
    send_temperature()
    time.sleep(2)  # Delay for 2 seconds

