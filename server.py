#!/usr/bin/python
from subprocess import call
import pcd8544.lcd as lcd
import time, os, sys
import wiringpi2 as wiringpi
import photo
import comm_server

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

ON, OFF = [1, 0]
BUTTON_GPIO = 0
INPUT = 0

def init():
  lcd.init()
  lcd.cls()
  lcd.backlight(ON)

  wiringpi.pinMode(BUTTON_GPIO,INPUT)

def get_time():
  date = time.strftime("%Y-%b-%d", time.localtime())
  hour = time.strftime("%H:%M:%S", time.localtime())
  return date+"_"+hour 

def display_main_screen():
  lcd.cls()
  lcd.centre_text(1,"Press shutter button")

def main_loop():
  display_main_screen()
  while 1:
    key = wiringpi.digitalRead(BUTTON_GPIO)
    if key == 1:
      now = get_time()
      comm_server.send_to_client(now)
      photo.take_photo(now)
      display_main_screen()
    time.sleep(0.2)

try:
  init()
  main_loop()

finally:
  for i in range(256,0,-16):
    lcd.set_brightness(i)
    time.sleep(0.025)
  lcd.cls()
  lcd.backlight(OFF)


