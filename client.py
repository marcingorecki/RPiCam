import serial
import time

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

while True:
    waiting = port.inWaiting()
    if(waiting > 0): 
	data = port.read(waiting)
	print data
    print "."
    time.sleep(1)
