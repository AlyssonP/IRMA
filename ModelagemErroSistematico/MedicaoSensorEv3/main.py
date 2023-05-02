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

# Create your objects here.
ev3 = EV3Brick()

nomeMed = str(input("Qual cor deseja medir? "))
ev3.speaker.beep()
Escrever = open(nomeMed+'.txt','a')

while(Button.CENTER not in ev3.buttons.pressed()):
    left = sensorLeft.rgb()
    right = sensorRight.rgb()

    lr= left[0]
    lg= left[1]
    lb= left[2]

    rr = right[0]
    rg = right[1]
    rb = right[2]

    # l = [lr,lg,lb, rr, rg, rb]
    Escrever.write(str(lr)+","+str(lg)+","+str(lb)+","+str(rr)+","+str(rg)+","+str(rb)+";")

Escrever.close()

# Write your program here.
ev3.speaker.beep()
