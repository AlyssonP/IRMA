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

dados = lerValoresArquivo("amarelo.txt")
media = calcularMedia(dados)
print(media)