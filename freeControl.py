#!/usr/bin/env python
#
 
import nxt
import sys
import tty, termios
import nxt.locator
from nxt.sensor import *
from nxt.motor import *
 
brick = nxt.locator.find_one_brick()
left = nxt.Motor(brick, PORT_B)
right = nxt.Motor(brick, PORT_C)
both = nxt.SynchronizedMotors(left, right, 0)
camera = nxt.Motor(brick, PORT_A)
leftboth = nxt.SynchronizedMotors(left, right, 100)
rightboth = nxt.SynchronizedMotors(right, left, 100)
guideLight = nxt.Light(brick, PORT_4)
backSense = nxt.Ultrasonic(brick, PORT_1)
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
ch = ' '
print "Ready"
while ch != 'q':
    ch = getch()
 
    if ch == 'w':
        print "Forwards"
        both.turn(100, 360, False)
    elif ch == 's':
        print "Backwards"
        both.turn(-100, 360, False)
        print 'Backup Room:', backSense.get_sample()
    elif ch == 'a':
        print "Left"
        leftboth.turn(100, 90, False)
    elif ch == 'd':
        print "Right"
        rightboth.turn(100, 90, False)
    elif ch == 'l':
        print "Light On"
        guideLight.set_illuminated(True)
    elif ch == 'b':
        print 'Space behind:', backSense.get_sample() 
    elif ch == '1':
        print "Camera Down"
        camera.turn(15, 15, False)
    elif ch == '2':
        print "Camera Up"
        camera.turn(-15, 15, False)
print "Finished"
