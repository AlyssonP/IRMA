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

sensorLeft =  ColorSensor(Port.S1)
sensorRight = ColorSensor(Port.S4)

def leituraSensor():
    left = sensorLeft.rgb()
    right = sensorRight.rgb()
    return [left,right]

def sigma(m2,n,M):
    return (m2/n - M**2)**(1/2)

def Mi(m,n):
    return m/n

def calculoMS(n):
    left = sensorLeft.rgb()
    right = sensorRight.rgb()
    m = [0, 0, 0]
    m2 = [0, 0, 0]
    ml = [0, 0, 0]
    m2l = [0, 0, 0]
    for i in range(n):
        s = left
        for l in range(3):
            ml[l] += s[l]
            m2l[l] += s[l]**2
        s = right
        for r in range(3):
            m[r] += s[r]
            m2[r] += s[r]**2

    M = [Mi(ml[0],n), Mi(ml[1],n), Mi(ml[2],n), Mi(m[0],n), Mi(m[1],n), Mi(m[2],n)]
    S = [sigma(m2l[0],n,M[0]), sigma(m2l[1],n,M[1]), sigma(m2l[2],n,M[2]), sigma(m2[0],n,M[3]), sigma(m2[1],n,M[4]), sigma(m2[2],n,M[5])]
    
    return M, S


# Create your objects here.
ev3 = EV3Brick()

cores = {}

while(Button.CENTER not in ev3.buttons.pressed()):
    buttoes = ev3.buttons.pressed()
    if(Button.LEFT in buttoes):
        cor = str(input("Qual cor vai medir? "))
        res = calculoMS(50)
        cores[cor] = res
        print("Sensor Left")
        print("Sigma:",res[1][:3])
        print("Mi:",res[0][:3])
        print("Sensor Right")
        print("Sigma:",res[1][3:])
        print("Mi:",res[0][3:])
    if(Button.RIGHT in buttoes):
        left = sensorLeft.rgb()
        right = sensorRight.rgb()
        for cor, valores in cores.items():
            if(((valores[0][0] - valores[1][0] <= left[0] >= valores[0][0] + valores[1][0]) and 
               (valores[0][1] - valores[1][1] <= left[1] >= valores[0][1] + valores[1][1]) and 
               (valores[0][2] - valores[1][2] <= left[2] >= valores[0][2] + valores[1][2])) and
               ((valores[0][3] - valores[1][3] <= right[0] >= valores[0][3] + valores[1][3]) and 
               (valores[0][4] - valores[1][4] <= right[1] >= valores[0][4] + valores[1][4]) and 
               (valores[0][5] - valores[1][5] <= right[2] >= valores[0][5] + valores[1][5]))):
                print(cor)


# Write your program here.
ev3.speaker.beep()