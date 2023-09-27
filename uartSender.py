import serial
import time

ser = serial.Serial(
    port='/dev/serial0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

while 1:
    ser.write(b'Hello, Raspberry!\n')
    time.sleep(1)

