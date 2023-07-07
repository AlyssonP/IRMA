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

def Sig(m2,n,M):
    return (m2/n - M**2)**(1/2)

def Mi(m,n):
    return m/n

def leituraCorErroAleatorio(ev3, corLeft, corRight, iteracoes):
    corRLM, corGLM, corBLM, corRRM, corGRM, corBRM = 0,0,0,0,0,0
    corRLM2, corGLM2, corBLM2, corRRM2, corGRM2, corBRM2 = 0,0,0,0,0,0

    for i in range(iteracoes):
        medicaoLeft = corLeft.rgb()
        medicaoRight = corRight.rgb()
        
        corRLM += medicaoLeft[0]
        corGLM += medicaoLeft[1]
        corBLM += medicaoLeft[2]
        corRLM2 += (medicaoLeft[0]**2)
        corGLM2 += (medicaoLeft[1]**2)
        corBLM2 += (medicaoLeft[2]**2)

        corRRM += medicaoRight[0]
        corGRM += medicaoRight[1]
        corBRM += medicaoRight[2]
        corRRM2 += (medicaoRight[0]**2)
        corGRM2 += (medicaoRight[1]**2)
        corBRM2 += (medicaoRight[2]**2)
    
    mi = [Mi(corRLM/iteracoes),Mi(corGLM/iteracoes),Mi(corBLM/iteracoes),
          Mi(corRRM/iteracoes),Mi(corGRM/iteracoes),Mi(corBRM/iteracoes)]
    
    sig = [Sig(corRLM2,iteracoes,mi[0]),
           Sig(corGLM2,iteracoes,mi[1]),
           Sig(corBLM2,iteracoes,mi[2]),
           Sig(corRRM2,iteracoes,mi[3]),
           Sig(corGRM2,iteracoes,mi[4]),
           Sig(corBRM2,iteracoes,mi[5])]
    
    return (mi, sig)

def compararCorErroAleatorio(medicaoLeft, medicaoRight, corReferencia):
    x = 3
    (mi, sig) = corReferencia
    if(((mi[0] - (sig[0]*x)) <= medicaoLeft[0]  <= (mi[0] + (sig[0]*x))) and
       ((mi[1] - (sig[1]*x)) <= medicaoLeft[1]  <= (mi[1] + (sig[1]*x))) and
       ((mi[2] - (sig[2]*x)) <= medicaoLeft[2]  <= (mi[2] + (sig[2]*x))) and
       ((mi[3] - (sig[3]*x)) <= medicaoRight[0] <= (mi[3] + (sig[3]*x))) and
       ((mi[4] - (sig[4]*x)) <= medicaoRight[1] <= (mi[4] + (sig[4]*x))) and
       ((mi[5] - (sig[5]*x)) <= medicaoRight[2] <= (mi[5] + (sig[5]*x)))):
        return True
    return False

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
        res = leituraCorErroAleatorio(ev3,sensorLeft,sensorRight)
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
            if(compararCorErroAleatorio(left, right, valores)):
                falar = cor
                ev3.speaker.beep()
        print("Você mostrou:",falar)
        #ev3.speaker.say(falar)


# Write your program here.
ev3.speaker.beep()