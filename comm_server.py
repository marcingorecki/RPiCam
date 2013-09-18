import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

def send_to_client(cmd):
    port.write(cmd)

