RPiCam
======

Project aims to create simple 3d camera using two Raspberry Pis. UI consists of PCD8544 display and a shutter button. More buttons will be added soon.

RPis are configured in master-slave configuration. Master maintains UI and notifies slave when to take a picture. 

Conversion of two jpgs to 3d file (.mpo) will be done on a PC. 

![RPiCam3D.jpg](/docs/RPiCam3D.jpg)

Components:
* https://github.com/XavierBerger/pcd8544/ + pcd8544 display from dx.com
* http://wiringpi.com/
* 2 x Raspberry Pi connected by Serial ports
* 2 x Raspberry Pi Camera
* 1 x switch (with pull down resistor http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/)
* Breadboard, wires
* Battery 

Configuration:
* Install required components
* On default image serial port is set to terminal. Disable it by removing getty on /dev/ttyAMA0 in /etc/inittab
