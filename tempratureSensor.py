# Install the Adafruit DHT library by executing the following command:
# sudo pip3 install Adafruit_DHT


import Adafruit_DHT


# Wiring: Connect the DHT11 module to your Raspberry Pi 4 using the following connections:
    # VCC of DHT11 to 5V of Raspberry Pi
    # GND of DHT11 to GND of Raspberry Pi
    # Data pin of DHT11 to GPIO4 


# Define the sensor type and the pin it's connected to
sensor = Adafruit_DHT.DHT11
pin = 4

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print(f'Temp={temperature:.1f}*C  Humidity={humidity:.1f}%')
    else:
        print('Failed to get reading. Try again!')

if __name__ == '__main__':
    while True:
        read_sensor()

