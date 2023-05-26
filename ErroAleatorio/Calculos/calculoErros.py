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

def calculoMS(cor):
    m = 0
    m2 = 0
    for i in cor:
        m += i
        m2 += i**2

    M = m/len(cor)
    S = (m2/len(cor) - M**2)**(1/2)
    return M, S

def calculoMSCor(vector,p):
    m = 0
    m2 = 0
    for i in range(len(vector)):
        m += vector[i][p]
        m2 += vector[i][p]**2

    M = m/len(vector)
    S = (m2/len(vector) - M**2)**(1/2)
    return M, S

def calcularMiSgimaCor(vector):
    m = [0, 0, 0]
    m2 = [0, 0, 0]
vermelho = lerValoresArquivo("coresLidas/vermelho.txt")
rlVermelho = calculoMSCor(vermelho,0)
glVermelho = calculoMSCor(vermelho,1)
blVermelho = calculoMSCor(vermelho,2)
print(rlVermelho)
print(glVermelho)
print(blVermelho)
# mediaVermelho = calcularMedia(lerValoresArquivo("coresLidas/vermelho.txt"))
# mediaAzul = calcularMedia(lerValoresArquivo("coresLidas/azul.txt"))
# mediaAzulClaro = calcularMedia(lerValoresArquivo("coresLidas/azulClaro.txt"))
# mediaRosa = calcularMedia(lerValoresArquivo("coresLidas/rosa.txt"))
# mediaVerde = calcularMedia(lerValoresArquivo("coresLidas/verde.txt"))
# mediaOutroVerde = calcularMedia(lerValoresArquivo("coresLidas/outroVerde.txt"))
# mediaAmarelo = calcularMedia(lerValoresArquivo("coresLidas/amarelo.txt"))
# mediaOutroAmarelo = calcularMedia(lerValoresArquivo("coresLidas/outroAmarelo.txt"))

# valores = [mediaVermelho, mediaAzul, mediaAzulClaro, mediaRosa, mediaVerde, mediaOutroVerde, mediaAmarelo, mediaOutroAmarelo]