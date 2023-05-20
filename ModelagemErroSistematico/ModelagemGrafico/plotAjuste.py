import matplotlib.pyplot as plt
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

# Calcula Z =[ y - f(x) ]
def Z(y, x, teta):
    z = np.zeros_like(y)
    for i in range(len(y)):
        z[i] = y[i] - (teta[0]*x[i] + teta[1])
    return z

# Calcula o Jacobiano
def J(x, teta):
    jacobian = np.zeros((len(x), len(teta)))
    # calculo do Jacobiano da funcao de erro
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
    rRed = np.array(rgbR[0])
    lRed = np.array(rgbL[0])
    # Green
    rGreen = np.array(rgbR[1])
    lGreen = np.array(rgbL[1])
    # Blue
    rBlue = np.array(rgbR[2])
    lBlue = np.array(rgbL[2])

    # Função de ajuste
    yR = lRed - rRed
    xR = lRed
    estadoRed = GaussNewtonI(yR,xR,[1,0],100)

    yG = lGreen - rGreen
    xG = lGreen
    estadoGreen = GaussNewtonI(yG,xG,[1,0],100)

    yB = lBlue - rBlue
    xB = lBlue
    estadoBlue = GaussNewtonI(yB,xB,[1,0],100)

    # Plotragem do gráfico das mediações não ajustadas
    plt.figure()
    plt.subplot(3,1,1)
    plt.scatter(rRed,lRed, facecolors='none', edgecolors='r')
    plt.scatter(rRed,rRed, color="red")
    
    plt.title("Gráficos de medições Sem ajute:", fontsize=10)

    plt.subplot(3,1,2)
    plt.scatter(rGreen,lGreen, facecolors='none', edgecolors='g')
    plt.scatter(rGreen,rGreen, color="green")

    plt.subplot(3,1,3)
    plt.scatter(rBlue,lBlue, facecolors='none', edgecolors='b')
    plt.scatter(rBlue,rBlue, color="blue")

    # plotar o gráfico das funções ajustadas
    plt.figure()
    plt.subplot(3,1,1)
    X = rRed
    Y = estadoRed[0]*X+estadoRed[1]
    plt.scatter(rRed,lRed-rRed, color="red")
    titulo = "erro(x) = {}x + {}".format(estadoRed[0], estadoRed[1])
    plt.plot(X, Y, 'red')
    plt.title(titulo, fontsize=10)

    plt.subplot(3,1,2)
    X = rGreen
    Y = estadoGreen[0]*X+estadoGreen[1]
    plt.scatter(rGreen,lGreen-rGreen, color="green")
    titulo = "erro(x) = {}x + {}".format(estadoGreen[0], estadoGreen[1])
    plt.plot(X, Y, 'green')
    plt.title(titulo, fontsize=10)

    plt.subplot(3,1,3)
    X = rBlue
    Y = estadoBlue[0]*X+estadoBlue[1]
    plt.scatter(rBlue,lBlue-rBlue, color="blue")
    titulo = "erro(x) = {}x + {}".format(estadoGreen[0], estadoGreen[1])
    plt.plot(X, Y, 'blue')
    plt.title(titulo, fontsize=10)

    # Plotragem do gráfico das mediações ajustadas
    plt.figure()
    plt.subplot(3,1,1)
    correcaoRed = lRed - (estadoRed[0]*lRed + estadoRed[1])
    plt.scatter(rRed,correcaoRed, facecolors='none', edgecolors='r')
    plt.scatter(rRed,rRed, color="red")

    plt.title("Gráficos de medições Com ajute:", fontsize=10)

    plt.subplot(3,1,2)
    correcaoGreen = lGreen - (estadoGreen[0]*lGreen + estadoGreen[1])
    plt.scatter(rGreen,correcaoGreen, facecolors='none', edgecolors='g')
    plt.scatter(rGreen,rGreen, color="green")

    plt.subplot(3,1,3)
    correcaoBlue = lBlue - (estadoBlue[0]*lBlue + estadoBlue[1])
    plt.scatter(rBlue,correcaoBlue, facecolors='none', edgecolors='b')
    plt.scatter(rBlue,rBlue, color="blue")

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