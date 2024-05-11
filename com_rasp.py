import serial
import time 

ser = serial.Serial('/dev/ttyS0', baudrate=9600,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     bytesize=serial.EIGHTBITS,
                     timeout=1000
                     )
data = 42
while True:
	ser.write(data.to_bytes(2, byteorder='little'))
	time.sleep(1)
	
	
ser.close()

