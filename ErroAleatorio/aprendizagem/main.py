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


sensorLeft =  ColorSensor(Port.S3)
sensorRight = ColorSensor(Port.S2)

def sigma(m2,n,M):
    return (m2/n - M**2)**(1/2)

def Mi(m,n):
    return m/n

def calculoMS(n, sensores):
    (sensorLeft, sensorRight) = sensores
    m = [0, 0, 0]
    m2 = [0, 0, 0]
    ml = [0, 0, 0]
    m2l = [0, 0, 0]
    for i in range(n):
        ll = sensorLeft.rgb()
        for l in range(3):
            ml[l] += ll[l]
            m2l[l] += ll[l]**2
        
        lr = sensorRight.rgb()
        for r in range(3):
            m[r] += lr[r]
            m2[r] += lr[r]**2

    M = [Mi(ml[0],n), Mi(ml[1],n), Mi(ml[2],n), Mi(m[0],n), Mi(m[1],n), Mi(m[2],n)]
    S = [sigma(m2l[0],n,M[0]), sigma(m2l[1],n,M[1]), sigma(m2l[2],n,M[2]), sigma(m2[0],n,M[3]), sigma(m2[1],n,M[4]), sigma(m2[2],n,M[5])]
    
    return M, S


# Create your objects here.
ev3 = EV3Brick()

cores = {}

ev3.speaker.beep()

#ev3.speaker.set_speech_options('pt-br','m3')

sensores = (sensorLeft, sensorRight)

print("Escolha as opções: LEFT(ler) e RIGHT(diz)")
while(Button.CENTER not in ev3.buttons.pressed()):
    buttoes = ev3.buttons.pressed()
    if(Button.LEFT in buttoes):
        ev3.speaker.beep()
        cor = str(input("Qual cor vai medir? "))
        res = calculoMS(800, sensores)
        cores[cor] = res
        print("Nova cor aprendida!")

    if(Button.RIGHT in buttoes):
        ev3.speaker.beep()
        left = sensorLeft.rgb()
        right = sensorRight.rgb()
        falar = "Não entendi, como é amigo?"
        for cor, valores in cores.items():
            print("cor: ",valores)
            print("left: ",left," | right: ",right)
            print(valores[1][0]*10)
            # if(((valores[0][0] - (valores[1][0]*10) <= left[0] <= (valores[0][0]) + valores[1][0]*10) and 
            #    (valores[0][1] - (valores[1][1]*10) <= left[1]  <= (valores[0][1]) + valores[1][1]*10) and 
            #    (valores[0][2] - (valores[1][2]*10) <= left[2]  <= (valores[0][2]) + valores[1][2]*10)) and
            #    ((valores[0][3] - (valores[1][3]*10) <= right[0] <= (valores[0][3]) + valores[1][3]*10) and 
            #    (valores[0][4] - (valores[1][4]*10) <= right[1] <= (valores[0][4]) + valores[1][4]*10) and 
            #    (valores[0][5] - (valores[1][5]*10) <= right[2] <= (valores[0][5]) + valores[1][5]*10))):
            if((valores[0][0] - 10 <= right[0] <= (valores[0][0]) + 10) and 
               (valores[0][1] - 10 <= right[1]  <= (valores[0][1]) + 10) and 
               (valores[0][2] - 10 <= right[2]  <= (valores[0][2]) + 10) and
               (valores[0][3] - 10 <= left[0] <= (valores[0][3]) + 10) and 
               (valores[0][4] - 10 <= left[1] <= (valores[0][4]) + 10) and 
               (valores[0][5] - 10 <= left[2] <= (valores[0][5]) + 10)):
                falar = cor
                ev3.speaker.beep()
        print("Você mostrou:",falar)
        #ev3.speaker.say(falar)


# Write your program here.
ev3.speaker.beep()