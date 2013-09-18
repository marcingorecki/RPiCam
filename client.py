import serial
import time
import photo

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

while True:
    waiting = port.inWaiting()
    if(waiting > 0): 
	data = port.read(waiting)
        photo.take_photo(data)
        print "Saved photo "+data
    time.sleep(0.1)
