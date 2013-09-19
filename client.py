import serial
import time
import photo
import common

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

while True:
    waiting = port.inWaiting()
    if(waiting > 0): 
	data = port.read(waiting)
        if data == "QUIT":
	   common.shutdown()	
        photo.take_photo(data)
        print "Saved photo "+data
    time.sleep(0.1)
