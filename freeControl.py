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
guideLight = nxt.Color20(brick, PORT_4)
backSense = nxt.Ultrasonic(brick, PORT_1)
sens = 360
sensTurn = 90
curSens = 5
power = 100
blue = Type.COLORBLUE
green = Type.COLORGREEN
red = Type.COLORRED
off = Type.COLORNONE
curCol = green
camDeg = 0


 
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
        both.turn(power, sens, False)
    elif ch == 's':
        print "Backwards"
        both.turn(-power, sens, False)
        print 'Backup Room:', backSense.get_sample()
    elif ch == 'a':
        print "Left"
        leftboth.turn(100, sensTurn, False)
    elif ch == 'd':
        print "Right"
        rightboth.turn(100, sensTurn, False)
    elif ch == 'l':
        curCol = red
        guideLight.set_light_color(curCol)
        print "Light On"
    elif ch == 'o':
        curCol = off
        guideLight.set_light_color(curCol)
        print "Light Off"
    elif ch == 't':
        if curCol == 16:
            curCol = red
            guideLight.set_light_color(curCol)
            print 'Light is red'
        elif curCol == 14:
            curCol = green
            guideLight.set_light_color(curCol)
            print 'Light is green'
        elif curCol == 15:
            curCol = blue
            guideLight.set_light_color(curCol)
            print 'Light is blue'
        else:
            print 'Light is off'
    elif ch == 'b':
        print 'Space behind:', backSense.get_sample()
    elif ch == 'e':
        if camDeg == 0:
            print "Camera cannot go lower"
        else:
            print "Camera Down:", camDeg
            camera.turn(25, 20, True)
            camDeg = camDeg - 1
    elif ch == 'r':
        if camDeg == 3:
            print "Camera cannot go higher"
        else:
            print "Camera Up:", camDeg
            camera.turn(-25, 20, True)
            camDeg = camDeg + 1
    elif ch == '1':
        sens = 45
        sensTurn = 50
        curSens = 1
        power = 65
        print "Sensitivity: 1"
    elif ch == '2':
        sens = 90
        sensTurn = 60
        curSens = 2
        power = 100
        print "Sensitivity: 2"
    elif ch == '3':
        sens = 180
        sensTurn = 70
        curSens = 3
        power = 100
        print "Sensitivity: 3"
    elif ch == '4':
        sens = 270
        sensTurn = 80
        curSens = 4
        power = 100
        print "Sensitivity: 4"
    elif ch == '5':
        sens = 360
        sensTurn = 90
        curSens = 5
        power = 100
        print "Sensitivity: 5"
    elif ch == '6':
        sens = 450
        sensTurn = 100
        curSens = 6
        power = 100
        print "Sensitivity: 6"
    elif ch == '7':
        sens = 540
        sensTurn = 110
        curSens = 7
        power = 100
        print "Sensitivity: 7"
    elif ch == '8':
        sens = 6930
        sensTurn = 120
        curSens = 8
        power = 100
        print "Sensitivity: 8"
    elif ch == '9':
        sens = 720
        sensTurn = 130
        curSens = 9
        power = 100
        print "Sensitivity: 9"
    elif ch == '0':
        sens = 810
        sensTurn = 140
        curSens = 10
        power = 100
        print "Sensitivity: 10"
    elif ch == 'c':
        print 'Current sensitivity is:',curSens
    elif ch == 'z':
        rightboth.turn(100, 3600, False)
        leftboth.turn(-100, 3600, False)
        print "Spin"
if camDeg == 3:
    camera.turn(25, 60, False)
elif camDeg == 2:
    camera.turn(25, 40, False)
elif camDeg == 1:
    camera.turn(25, 20, False)
guideLight.set_light_color(off)
print "Finished"
