import serial

receiver = serial.Serial(
     port='COM5',
     baudrate=9600,
     parity=serial.PARITY_NONE,
     stopbits=serial.STOPBITS_ONE,
     bytesize=serial.EIGHTBITS,
     timeout=0.5,
     )


while True:
    rawData = receiver.readline()
    print(rawData.hex())