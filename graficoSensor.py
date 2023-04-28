import matplotlib.pyplot as plt

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
    
    plt.subplot(3,1,1)
    plt.plot(rgbL[0], marker = 'o', linestyle = 'none', mec = "r", mfc="r")
    plt.plot(rgbR[0], marker = 'o', linestyle = 'none', mec = "r", mfc = 'w')

    plt.subplot(3,1,2)
    plt.plot(rgbL[1], marker = 'o', linestyle = 'none', mec = 'g', mfc='g')
    plt.plot(rgbR[1], marker = 'o', linestyle = 'none', mec = 'g', mfc = 'w')

    plt.subplot(3,1,3)
    plt.plot(rgbL[2], marker = 'o', linestyle = 'none', mec = 'b', mfc = 'b')
    plt.plot(rgbR[2], marker = 'o', linestyle = 'none', mec = 'b', mfc = 'w')
    plt.show()


mediaVermelho = calcularMedia(lerValoresArquivo("vermelho.txt"))
mediaAmarelo = calcularMedia(lerValoresArquivo("amarelo.txt"))
mediaAzul = calcularMedia(lerValoresArquivo("azul.txt"))

print("Medias cor Vermelho:",mediaVermelho)
print("Medias cor Amarelo:",mediaAmarelo)
print("Medias cor Azul:",mediaAzul)
valores = [mediaVermelho, mediaAmarelo, mediaAzul]
desenharGraficoRGB(valores)