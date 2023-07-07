#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create the sensors and motors objects
ev3 = EV3Brick()

import time

TKEYPRESS = 250

def detectMotoresSensores(ev3, falar):
    # Motores
    try:
        motorLeft = Motor(Port.A)
    except OSError:
        if falar:
            ev3.speaker.say("Motor esquerdo não encontrado.")
            ev3.speaker.say("Conecte o motor esquerdo na porta D")
        return
    try:
        motorRight = Motor(Port.B)
    except OSError:
        if falar:
            ev3.speaker.say("Motor direito não encontrado.")
            ev3.speaker.say("Conecte o motor direito na porta A")
        return
    
    if falar:
        ev3.speaker.say("Motores encontrados")
    
    # Sensores
    infrared = None
    try:
        infrared = InfraredSensor(Port.S2)
    except:
        if falar:
            ev3.speaker.say("Sensor infravermelho não encontrado.")
            ev3.speaker.say("Conecte o sensor infravermelho na porta S1")
        
    
    try:
        corLeft = ColorSensor(Port.S1)
    except OSError:
        if falar:
            ev3.speaker.say("Sensor de cor esquerdo não encontrado.")
            ev3.speaker.say("Conecte o sensor de cor esquerdo na porta S3")
        return
    
    try: 
        corRight  = ColorSensor(Port.S4)
    except OSError:
        if falar:
            ev3.speaker.say("Sensor de cor direito não encontrado.")
            ev3.speaker.say("Conecte o sensor de cor direito na porta S2")
        return
    
    if falar:
        ev3.speaker.say("Sensores encontrados")
    
    return (motorLeft, motorRight,infrared, corLeft, corRight)

def passear(ev3, MotorSensor):
    (motorLeft, motorRight, infrared, corLeft, corRight) = MotorSensor
    
    while(True):
        botoes = ev3.buttons.pressed()
        #Botoes
        if(Button.UP in botoes):
            motorRight.run(200)
            motorLeft.run(200)

        if(Button.DOWN in botoes):
            motorRight.run(-200)
            motorLeft.run(-200)

        if(Button.LEFT in botoes):
            motorRight.run(200)
            motorLeft.run(-200)

        if(Button.RIGHT in botoes):
            motorRight.run(-200)
            motorLeft.run(200)

        if(Button.CENTER in botoes):
            motorRight.brake()
            motorLeft.brake()
            break

        if(infrared != None and infrared.distance()<= 10):
            motorRight.brake()
            motorLeft.brake() 
    ev3.speaker.say("Fim do passeio!")

def leituraCor(ev3, corLeft, corRight, iteracoes):
    (corRL, corGL, corBL, corRR, corGR, corBR) = (0,0,0,0,0,0)
    for i in range(iteracoes):
        medicaoLeft = corLeft.rgb()
        medicaoRight = corRight.rgb()
        
        corRL += medicaoLeft[0]
        corGL += medicaoLeft[1]
        corBL += medicaoLeft[2]

        corRR += medicaoRight[0]
        corGR += medicaoRight[1]
        corBR += medicaoRight[2]
    
    corRL = corRL/iteracoes
    corGL = corGL/iteracoes
    corBL = corBL/iteracoes

    corRR = corRR/iteracoes
    corGR = corGR/iteracoes
    corBR = corBR/iteracoes

    return (corRL, corGL, corBL, corRR, corGR, corBR)
        
def salvaCalibracao(leitura,nome):
    (corRL, corGL, corBL, corRR, corGR, corBR) = leitura
    arquivo = open(nome+".csv", "w")
    arquivo.write(str(corRL)+";"+str(corGL)+";"+str(corBL)+";"+str(corRR)+";"+str(corGR)+";"+str(corBR))
    arquivo.close()

def aprendizagem(ev3, MotorSensor):
    (motorLeft, motorRight,infrared, corLeft, corRight) = MotorSensor
    referenciaCores = {}
    opcoes = {"LEFT":"Cor VIRA ESQUERDA", "RIGHT":"Cor VIRA DIREITA", "UP":"COR PARAR", "CENTER":"PARAR APRENDIZADO"}
    menu(ev3, opcoes)
    while(True):
        botoes = ev3.buttons.pressed()
        if(Button.LEFT in botoes):
            ev3.speaker.say("Aprendendo a cor ViraEsquerda")
            corViraEsquerda = leituraCor(ev3, corLeft, corRight, 100)
            referenciaCores["VIRAESQUERDA"] = corViraEsquerda
            print(corViraEsquerda)
            ev3.speaker.beep()
            
        if(Button.RIGHT in botoes):
            ev3.speaker.say("Aprendendo a cor ViraDireira")
            corViraDireira = leituraCor(ev3, corLeft, corRight, 100)
            referenciaCores["VIRADIREITA"] = corViraDireira
            print(corViraDireira)
            ev3.speaker.beep()
        
        if(Button.UP in botoes):
            ev3.speaker.say("Aprendendo a cor PARAR")
            corParar = leituraCor(ev3, corLeft, corRight, 100)
            referenciaCores["PARADO"] = corParar
            print(corParar)
            ev3.speaker.beep()
            
        if(Button.CENTER in botoes):
            ev3.speaker.say("Aprendizado finalizado")
            break
    return referenciaCores

def compararCor(medicaoLeft, medicaoRight, corReferencia):
    sig = 2
    if((medicaoLeft[0] - sig <= corReferencia[0] <= medicaoLeft[0] + sig) and
       (medicaoLeft[1] - sig <= corReferencia[1] <= medicaoLeft[1] + sig) and
       (medicaoLeft[2] - sig <= corReferencia[2] <= medicaoLeft[2] + sig) and
       (medicaoRight[0] - sig <= corReferencia[3] <= medicaoRight[0] + sig) and
       (medicaoRight[1] - sig <= corReferencia[4] <= medicaoRight[1] + sig) and
       (medicaoRight[2] - sig <= corReferencia[5] <= medicaoRight[2] + sig)):
        return True
    return False

def detectaNovoEstado(ev3, cronometro, estado, MotorSensor, parametros, referenciasCores):
    
    (motorLeft, motorRight, infrared, corLeft, corRight) = MotorSensor
    (PoCorL, KpL, PoMotorL, PoCorR, KpR, PoMotorR) = parametros

    novoEstado = estado
    botoes = ev3.buttons.pressed()

    if((Button.CENTER in botoes) and (estado == "PARADO")):
        novoEstado = "ANDANDO"
        PoCorL = corLeft.rgb()[2]
        PoCorR = corRight.rgb()[2]
    elif((Button.CENTER in botoes) and (estado == "ANDANDO")):
        novoEstado = "PARADO"
    elif((estado == "ANDANDO") and compararCor(corLeft.rgb(),corRight.rgb(), referenciasCores["VIRAESQUERDA"])):
        novoEstado = "VIRAESQUERDA"
    elif((estado == "ANDANDO") and compararCor(corLeft.rgb(),corRight.rgb(), referenciasCores["VIRADIREITA"])):
        novoEstado = "VIRADIREITA"
    elif((estado == "ANDANDO") and compararCor(corLeft.rgb(),corRight.rgb(), referenciasCores["PARADO"])):
        novoEstado = "PARADO"

    parametros = (PoCorL, KpL, PoMotorL, PoCorR, KpR, PoMotorR)
    return (novoEstado, parametros)

def executaEstado(ev3, MotorSensor, estado, parametros):
    (motorLeft, motorRight, infrared, corLeft, corRight) = MotorSensor
    (PoCorL, KpL, PoMotorL, PoCorR, KpR, PoMotorR) = parametros

    CorL = corLeft.rgb()[2]
    CorR = corRight.rgb()[2]
    if(estado == "ANDANDO"):
        if(CorL<10 and CorR<10): # Encruzilhada com preto
            # Anda em frente
            PotL = 50 
            PotR = 50
            motorLeft.dc(PotL)
            motorRight.dc(PotR)
            time.sleep(0.3)
        else:
            PotL = (PoCorL - CorL)*KpL + PoMotorL
            PotR = (PoCorR - CorR)*KpR + PoMotorR
            # Aqui é o seguinte. É preciso fazer uma correção da potência dos motores para evitar
            # uma "zona morta", onde a potência submetida é baixa demais e o motor efetivamente 
            # não faz nada. Para ficar mais fácil para os alunos eu vou fazer o ajuste com um if
            # mas o legal mesmo seria fazer a modelagem do erro sistemático
        
            #print(PotL, PotR)
            if(-40<PotL and PotL<10):
                PotL = -40
            if(-40<PotR and PotR<10):
                PotR = -40
            motorLeft.dc(PotL)
            motorRight.dc(PotR)
    elif(estado == "PARADO"):
        motorLeft.brake()
        motorRight.brake()
    elif(estado == "VIRAESQUERDA"):
        motorLeft.run(50)
        motorRight.run(50)
        time.sleep(0.4)
        motorLeft.brake()
        motorRight.brake()
        motorLeft.run(-100)
        motorRight.run(100)
        time.sleep(0.2)
    elif(estado == "VIRADIREITA"):
        motorLeft.run(50)
        motorRight.run(50)
        time.sleep(0.4)
        motorLeft.brake()
        motorRight.brake()
        motorLeft.run(100)
        motorRight.run(-100)
        time.sleep(0.2)
    elif(estado == "PARADO"):
        motorLeft.brake()
        motorRight.brake()

def segueFaixa(ev3, MotorSensor):
    (motorLeft, motorRight, infrared, corLeft, corRight) = MotorSensor   

    cronometro = 0

    contador = 0
    PoCorL = 0
    KpL = -1.7 # A diferença no ganho é por causa da assimetria dos sensores
    PoMotorL = 60

    PoCorR = 0
    KpR = -1.2
    PoMotorR = 60
    parametros = (PoCorL, KpL, PoMotorL, PoCorR, KpR, PoMotorR)
    referenciasCores = {}
    
    estado = "PARADO"
    while(True):
        NovoEstado, parametros = detectaNovoEstado(ev3, cronometro, estado, MotorSensor, parametros)
            
        executaEstado(ev3, MotorSensor, NovoEstado, parametros, referenciasCores)
            
        estado = NovoEstado

def menu(ev3, dicOpcoes):
    for botao, opcao in dicOpcoes.items():
        ev3.speaker.say("Botão "+botao+" : "+opcao)

def main():
    fala = False

    # Create your objects here.
    ev3 = EV3Brick()

    # Write your program here.
    ev3.speaker.set_speech_options('pt-br','m3')

    MotorSensor = detectMotoresSensores(ev3, fala)

    ev3.speaker.beep()
    opcoesMenuGeral = {"LEFT":"MODO PASSEAR","RIGHT":"MODO APRENDIZAGEM","UP":"SEGUE FAIXA","DOWN":"Finalizar Programa"}
    menu(ev3, opcoesMenuGeral)

    referenciasCores = {}
    while(True):
        botoes = ev3.buttons.pressed()
        if(Button.LEFT in botoes):
            ev3.speaker.say("Vamos passear")
            passear(ev3, MotorSensor)
        
        if(Button.RIGHT in botoes):
            if(referenciasCores.get("VIRAESQUERDA") == None and referenciasCores.get("VIRADIREITA") == None and referenciasCores.get("PARADO") == None):
                ev3.speaker.say("Modo aprendizagem, eu sou muito burro kk")
                referenciasCores = aprendizagem(ev3, MotorSensor)
                ev3.speaker.beep()
            else:
                ev3.speaker.say("Eu sou inteligente agora")
                ev3.speaker.beep()
        
        if(Button.UP in botoes):
            if(referenciasCores.get("VIRAESQUERDA") == None and referenciasCores.get("VIRADIREITA") == None and referenciasCores.get("PARADO") == None):
                ev3.speaker.say("Preciso aprender para andar")
                ev3.speaker.beep()
            else :
                ev3.speaker.say("Eu sei seguir faixa")
                segueFaixa(ev3, MotorSensor, referenciasCores)
                ev3.speaker.beep()
        
        if(Button.DOWN in botoes):
            ev3.speaker.say("Finalizando programa.")
            break

main()
ev3.speaker.beep()

"""
    PARA O ROBÔ CONSEGUIR SEGUIR FAIXA É PRECISO ENSINAR O ROBÔ
    ELE PODE CONTER UM BUGS, PORQUE NÃO FOI TESTE EM UM ROBÔ LEGO PESSOALMENTE
    
    DEV: ALYSSON. ESTUDANTE DE TSI
"""