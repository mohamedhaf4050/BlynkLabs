import serial

ser = serial.Serial(
    port='/dev/serial0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

while 1:
    incoming_data = ser.readline().decode('ascii')
    print(f'Received: {incoming_data}')

