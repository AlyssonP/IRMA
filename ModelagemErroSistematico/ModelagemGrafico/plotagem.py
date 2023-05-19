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

def calcularMedia(listaValores):
    l = [0,0,0,0,0,0]
    for lv in listaValores:
        for n in range(6):
            l[n] += lv[n]
    m = []
    for n in l:
        m.append(n/len(listaValores))
    return m

def Z(y, x, teta):
    z = np.zeros_like(y)
    for i in range(len(y)):
        z[i] = y[i] - (teta[0]*x[i] + teta[1])
    return z

def J(x, teta):
    jacobian = np.zeros((len(x), len(teta)))
    for i in range(len(x)):
        jacobian[i, :] = [-x[i], -1]
    return jacobian

def GaussNewtonI(Y, X, valorInicial, n):
    estado = list(valorInicial)
    for i in range(n):
        Z1 = Z(Y, X, estado)
        J1 = J(X, estado)
        # "J1.T" matriz transposta de J1, "@"" realiza a multiplicação matricial
        incremento = -np.linalg.inv(J1.T @ J1) @ J1.T @ Z1
        estado = estado + incremento
    return estado

def desenharGrafico(x, y1, y2, cor, pdGrafico):
    plt.subplot(pdGrafico[0],pdGrafico[1],pdGrafico[2])
    plt.scatter(x,y1, facecolors='none', edgecolors=cor)
    plt.scatter(x,y2, color=cor)


def calculoX(rgbL,rgbR):
    ve = np.array(rgbL)
    vv = np.array(rgbR)
    y = ve - vv #Erro sistematico
    x = np.array(rgbL)
    estado = GaussNewtonI(y,x,[1,0],100)
    eixoX = ve - (estado[0]*x + estado[1])
    return eixoX

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
    
    eixoR = calculoX(rgbL[0],rgbR[0])
    desenharGrafico(eixoR, rgbL[0], rgbR[0], "red", [3,1,1])

    eixoG = calculoX(rgbL[1],rgbR[1])
    desenharGrafico(eixoG, rgbL[1], rgbR[1], "green", [3,1,2])

    eixoB = calculoX(rgbL[2],rgbR[2])
    desenharGrafico(eixoB, rgbL[2], rgbR[2], "blue", [3,1,3])

    plt.show()

# minha medição no lab
mediaVermelho = calcularMedia(lerValoresArquivo("coresLidas/vermelho.txt"))
mediaAzul = calcularMedia(lerValoresArquivo("coresLidas/azul.txt"))
mediaAzulClaro = calcularMedia(lerValoresArquivo("coresLidas/azulClaro.txt"))
mediaRosa = calcularMedia(lerValoresArquivo("coresLidas/rosa.txt"))
mediaVerde = calcularMedia(lerValoresArquivo("coresLidas/verde.txt"))
mediaOutroVerde = calcularMedia(lerValoresArquivo("coresLidas/outroVerde.txt"))
mediaAmarelo = calcularMedia(lerValoresArquivo("coresLidas/amarelo.txt"))
mediaOutroAmarelo = calcularMedia(lerValoresArquivo("coresLidas/outroAmarelo.txt"))
valores = [mediaVermelho, mediaAzul, mediaAzulClaro, mediaRosa, mediaVerde, mediaOutroVerde, mediaAmarelo, mediaOutroAmarelo]

# Medição do professor
# mediaAmarelo = calcularMedia(lerValoresArquivoSCE("coresProfessor/amarelo.sce"))
# mediaAzul = calcularMedia(lerValoresArquivoSCE("coresProfessor/azul.sce"))
# mediaBranco = calcularMedia(lerValoresArquivoSCE("coresProfessor/branco.sce"))
# mediaCinza = calcularMedia(lerValoresArquivoSCE("coresProfessor/cinza.sce"))
# mediaCreme = calcularMedia(lerValoresArquivoSCE("coresProfessor/creme.sce"))
# mediaPreto = calcularMedia(lerValoresArquivoSCE("coresProfessor/preto.sce"))
# mediaVerde = calcularMedia(lerValoresArquivoSCE("coresProfessor/verde.sce"))
# mediaVermelho = calcularMedia(lerValoresArquivoSCE("coresProfessor/vermelho.sce"))

# valores = [mediaAmarelo,mediaAzul,mediaBranco,mediaCinza,mediaCreme,mediaPreto,mediaVerde ,mediaVermelho]

desenharGraficoRGB(valores)
