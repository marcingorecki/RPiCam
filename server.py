#!/usr/bin/python
from subprocess import call
import pcd8544.lcd as lcd
import time, os, sys
import wiringpi2 as wiringpi
import photo
import comm_server
import actions

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

ON, OFF = [1, 0]
BUTTON_OK = 0
BUTTON_FKEY = 6
INPUT = 0
current = 0

def init():
  lcd.init()
  lcd.cls()
  lcd.backlight(ON)

  wiringpi.pinMode(BUTTON_OK,INPUT)
  wiringpi.pinMode(BUTTON_FKEY,INPUT)

def display_main_screen():
  lcd.cls()
  lcd.centre_text(1,actions.get_text(current))

def main_loop():
  global current
  display_main_screen()
  while 1:
    key = wiringpi.digitalRead(BUTTON_OK)
    fkey = wiringpi.digitalRead(BUTTON_FKEY)
    if key == 1:
      #photo.take_sync_photo(comm_server, lcd)
      actions.run_command(current, comm_server, lcd)
      display_main_screen()
    if fkey == 1:
      print('fkey')
      current=(current+1)%actions.get_count()
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


