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
sens = 360
sensTurn = 90
 
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
print "Sensitivity: 5"
while ch != 'q':
    ch = getch()
 
    if ch == 'w':
        print "Forwards"
        both.turn(100, sens, False)
    elif ch == 's':
        print "Backwards"
        both.turn(-100, sens, False)
        print 'Backup Room:', backSense.get_sample()
    elif ch == 'a':
        print "Left"
        leftboth.turn(100, sensTurn, False)
    elif ch == 'd':
        print "Right"
        rightboth.turn(100, sensTurn, False)
    elif ch == 'l':
        print "Light On"
        guideLight.set_illuminated(True)
    elif ch == 'b':
        print 'Space behind:', backSense.get_sample() 
    elif ch == 'o':
        print "Camera Down"
        camera.turn(15, 15, False)
    elif ch == 'p':
        print "Camera Up"
        camera.turn(-15, 15, False)
    elif ch == '1':
        sens = 45
        sensTurn = 50
        print "Sensitivity: 1"
    elif ch == '2':
        sens = 90
        sensTurn = 60
    print "Sensitivity: 2"
    elif ch == '3':
        sens = 180
        sensTurn = 70
        print "Sensitivity: 3"
    elif ch == '4':
        sens = 270
        sensTurn = 80
        print "Sensitivity: 4"
    elif ch == '5':
        sens = 360
        sensTurn = 90
        print "Sensitivity: 5"
    elif ch == '6':
        sens = 450
        sensTurn = 100
        print "Sensitivity: 6"
    elif ch == '7':
        sens = 540
        sensTurn = 110
        print "Sensitivity: 7"
    elif ch == '8':
        sens = 6930
        sensTurn = 120
        print "Sensitivity: 8"
    elif ch == '9':
        sens = 720
        sensTurn = 130
        print "Sensitivity: 9"
    elif ch == '0':
        sens = 810
        sensTurn = 140
        print "Sensitivity: 10"
print "Finished"
