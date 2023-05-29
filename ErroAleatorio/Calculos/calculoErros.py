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
    sigma = []
    mi = []
    for i in range(6):
        cal = calculoMSCor(vector,i)
        mi.append(cal[0])
        sigma.append(cal[1])
    return mi, sigma

nomeCores = ["amarelo","azul","azulClaro","outroAmarelo","outroVerde","rosa","verde","vermelho"]
cores = {}
for cor in nomeCores:
    valoresCor = lerValoresArquivo("coresLidas/"+cor+".txt")
    cores[cor] = calcularMiSgimaCor(valoresCor)

for nome, valores in cores.items():
    print("Cor:",nome)
    print("Mi:",valores[0])
    print("Sigma:",valores[1])
