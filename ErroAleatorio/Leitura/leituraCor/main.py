#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

def valoresCor(n):
    cor  = []
    for i in range(n):

def sigma(m2,n,M)
    return (m2/n - M**2)**(1/2)

def Mi(m,n)
    return m/n

def calculoMS(n,lado):
    left = sensorLeft.rgb()
    right = sensorRight.rgb()
    m = [0, 0, 0]
    m2 = [0, 0, 0]
    ml = [0, 0, 0]
    m2l = [0, 0, 0]
    for i in range(n) :
        for l in range(3):
            s= left[l]
            ml[l] += s
            m2l[l] += s**2
        for r in range(3):
            s= right[r]
            m[r] += s
            m2[r] += s**2

    M = [Mi(ml[0],n), Mi(ml[1],n), Mi(ml[1],n), Mi(m[0],n), Mi(m[1],n), Mi(m[1],n)]
    S = [sigma(m2l[0,n,M[3]]), sigma(m2l[0,n,M[4]]), sigma(m2l[0,n,M[5]]), sigma(m2[0,n,M[0]]), sigma(m2[0,n,M[1]]), sigma(m2[0,n,M[2]])]
    
    return M, S

# Create your objects here.
ev3 = EV3Brick()

while(Button.CENTER not in ev3.buttons.pressed()):
    if(Button.LEFT in ev3.buttons.pressed()):
        cor = str(input("Qual cor vai medir? "))
        res = calculoMS(50)
        print("Sigma:",res[1])
        print("Mi:",res[0])


# Write your program here.
ev3.speaker.beep()