import matplotlib.pyplot as plt
import numpy as np

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
    
    # Cores
    # Red
    xrRed = np.array(rgbR[0])
    xlRed = np.array(rgbL[0])
    ylRed = np.array(rgbL[0])
    yrRed = np.array(rgbR[0])
    # Green
    xrGreen = np.array(rgbR[1])
    xlGreen = np.array(rgbL[1])
    ylGreen = np.array(rgbL[1])
    yrGreen = np.array(rgbR[1])
    # Blue
    xrBlue = np.array(rgbR[2])
    xlBlue = np.array(rgbL[2])
    ylBlue = np.array(rgbL[2])
    yrBlue = np.array(rgbR[2])


    plt.subplot(3,2,1)
    plt.scatter(xrRed,ylRed, facecolors='none', edgecolors='r')
    plt.scatter(xrRed,yrRed, color="red")

    plt.subplot(3,2,3)
    plt.scatter(xrGreen,ylGreen, facecolors='none', edgecolors='g')
    plt.scatter(xrGreen,yrGreen, color="green")

    plt.subplot(3,2,5)
    plt.scatter(xrBlue,ylBlue, facecolors='none', edgecolors='b')
    plt.scatter(xrBlue,yrBlue, color="blue")

    # valores de referência como também aos valores medidos
    plt.subplot(3,2,2)
    plt.scatter(xrRed,ylRed-yrRed, color="red", edgecolors='black')

    plt.subplot(3,2,4)
    plt.scatter(xrGreen,ylGreen-yrGreen, color="green", edgecolors='black')

    plt.subplot(3,2,6)
    plt.scatter(xrBlue,ylBlue-yrBlue, color="blue", edgecolors='black')

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

desenharGraficoRGB(valores)