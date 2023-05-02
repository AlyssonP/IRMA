import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Leitura de Arquivo SCE
def lerValoresArquivoSCE(nome):
    with open(nome) as ler:
        lista = ler.read().split(";\n")
    e = lista[0].split("\n")[2]
    lista[0] = e
    listaValores = []
    for l in lista[:-1]:
        aux = []
        for n in l.split():
            aux.append(float(n))
        listaValores.append(aux)
    return listaValores

def lerValoresArquivo(nome):
    with open(nome) as ler:
        lista = ler.read().split(";")
    listaValores = []
    for l in lista[:-1]:
        aux = []
        for n in l.split(","):
            aux.append(int(n))
        listaValores.append(aux)
    return listaValores

def calcularMedia(listaValores):
    l = [0,0,0,0,0,0]
    for lv in listaValores:
        for n in range(6):
            l[n] += lv[n]
    m = []
    for n in l:
        m.append(n/len(listaValores))
    return m

def modelo_linear(x, a, b):
    return a * x + b

def estimarValoresX(listaCorL, listaCorR, ladoVerdadeiro):
    valorV = np.array([])
    valorE = np.array([])
    # Verificando qual valor verdadeiro escolhido
    if (ladoVerdadeiro.lower() == 'left' or ladoVerdadeiro.lower() == 'l'):
        valorV = np.array(listaCorL)
        valorE = np.array(listaCorR)
    elif(ladoVerdadeiro.lower() == 'right' or ladoVerdadeiro.lower() == 'r'):
        valorV = np.array(listaCorR)
        valorE = np.array(listaCorL)
    
    e = valorE - valorV # Lista de Erros Sistemático das cores

    erroModular = np.fabs(e)
    # Buscando valor dos parametros A e B da função Linear
    valoresEstimados, MatrizConc = curve_fit(modelo_linear, valorE, erroModular)

    # Retorno dos valores do eixo X
    return modelo_linear(valorE, *valoresEstimados)

def desenharGraficoRGB(valores):
    rgbL = [[],[],[]]
    rgbR = [[],[],[]]
    for n in valores:
        # Red
        rgbL[0].append(n[0])
        rgbR[0].append(n[3])
        # Green
        rgbL[1].append(n[1])
        rgbR[1].append(n[4])
        # Blue
        rgbL[2].append(n[2])
        rgbR[2].append(n[5])
    
    ladoVerdadeiro = 'right'
    x = estimarValoresX(rgbL[0],rgbR[0],ladoVerdadeiro)

    plt.subplot(3,1,1)
    plt.scatter(x,rgbL[0], facecolors='none', edgecolors='r')
    plt.scatter(x,rgbR[0], color="red")

    
    x = estimarValoresX(rgbL[1],rgbR[1],ladoVerdadeiro)
    plt.subplot(3,1,2)
    plt.scatter(x,rgbL[1], facecolors='none', edgecolors='g')
    plt.scatter(x,rgbR[1], color="g")

    x = estimarValoresX(rgbL[2],rgbR[2],ladoVerdadeiro)
    plt.subplot(3,1,3)
    plt.scatter(x,rgbL[2], facecolors='none', edgecolors='b')
    plt.scatter(x,rgbR[2], color="b")

    plt.show()

mediaVermelho = calcularMedia(lerValoresArquivo("coresLidas/vermelho.txt"))
mediaAzul = calcularMedia(lerValoresArquivo("coresLidas/azul.txt"))
mediaAzulClaro = calcularMedia(lerValoresArquivo("coresLidas/azulClaro.txt"))
mediaRosa = calcularMedia(lerValoresArquivo("coresLidas/rosa.txt"))
mediaVerde = calcularMedia(lerValoresArquivo("coresLidas/verde.txt"))
mediaOutroVerde = calcularMedia(lerValoresArquivo("coresLidas/outroVerde.txt"))
mediaAmarelo = calcularMedia(lerValoresArquivo("coresLidas/amarelo.txt"))
mediaOutroAmarelo = calcularMedia(lerValoresArquivo("coresLidas/outroAmarelo.txt"))

valores = [mediaVermelho, mediaAzul, mediaAzulClaro, mediaRosa, mediaVerde, mediaOutroVerde, mediaAmarelo, mediaOutroAmarelo]

# mediaAmarelo = calcularMedia(lerValoresArquivoSCE("coresSce/amarelo.sce"))
# mediaAzul = calcularMedia(lerValoresArquivoSCE("coresSce/azul.sce"))
# mediaBranco = calcularMedia(lerValoresArquivoSCE("coresSce/branco.sce"))
# mediaCinza = calcularMedia(lerValoresArquivoSCE("coresSce/cinza.sce"))
# mediaCreme = calcularMedia(lerValoresArquivoSCE("coresSce/creme.sce"))
# mediaPreto = calcularMedia(lerValoresArquivoSCE("coresSce/preto.sce"))
# mediaVerde = calcularMedia(lerValoresArquivoSCE("coresSce/verde.sce"))
# mediaVermelho = calcularMedia(lerValoresArquivoSCE("coresSce/vermelho.sce"))

# valores = [mediaAmarelo,mediaAzul,mediaBranco,mediaCinza,mediaCreme,mediaPreto,mediaVerde ,mediaVermelho]

desenharGraficoRGB(valores)