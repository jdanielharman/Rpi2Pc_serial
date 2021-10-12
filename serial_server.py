import serial
import time
from random import randint

serialPort = serial.Serial(port='/dev/serial0', baudrate='115200', bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

cnt = 0
theta = 0
while 1:
	msg = f'theta: {theta} Dist: {randint(4,5)}\n'
	serialPort.write(msg.encode())
	time.sleep(0.000125)
	cnt += 1
	theta += 1
	theta = theta % 360
	print(f'\rcnt {cnt} msg {msg}', end='')
