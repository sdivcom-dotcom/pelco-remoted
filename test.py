import serial
import time
# Установить порт и скорость соединения
port = '/dev/ttyUSB1'  # Укажите свой COM-порт
baudrate = 2400
#A001 
#AF00
#16
ser = serial.Serial(port=port, baudrate=baudrate)
data = bytes.fromhex('A00101000000AF00')
ser.write(data)
time.sleep(1)
data = bytes.fromhex('A00100000000AF00')
ser.write(data)
