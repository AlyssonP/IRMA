RUIDO=       0.03

AMARELOR=	0.32
AMARELOG=	0.25
AMARELOB=	0.09

AZULR=		0.03
AZULG=		0.13
AZULB=		0.30

CINZAR=		0.18
CINZAG=		0.34
CINZAB=		0.40

CREMER=		0.29
CREMEG=		0.36
CREMEB=		0.42

PRETOR=		0.02
PRETOG=		0.05
PRETOB=		0.04

VERDER=		0.03
VERDEG=		0.19
VERDEB=		0.14

VERMELHOR=	0.26
VERMELHOG=	0.06
VERMELHOB=	0.04

def TOINT(A):
    return    int(round((A)*100.0))

try:
    while True:
        R, G, B = map(float, input().split())
        if(     (TOINT(AMARELOR-RUIDO) <= TOINT(R) and TOINT(R) <= TOINT(AMARELOR+RUIDO)) and
                (TOINT(AMARELOG-RUIDO) <= TOINT(G) and TOINT(G) <= TOINT(AMARELOG+RUIDO)) and
                (TOINT(AMARELOB-RUIDO) <= TOINT(B) and TOINT(B) <= TOINT(AMARELOB+RUIDO))):
                print("AMARELO")
        elif(   (TOINT(AZULR-RUIDO) <= TOINT(R) and TOINT(R) <= TOINT(AZULR+RUIDO)) and
                (TOINT(AZULG-RUIDO) <= TOINT(G) and TOINT(G) <= TOINT(AZULG+RUIDO)) and
                (TOINT(AZULB-RUIDO) <= TOINT(B) and TOINT(B) <= TOINT(AZULB+RUIDO))):
                print("AZUL")
        elif(   (TOINT(CINZAR-RUIDO) <= TOINT(R) and TOINT(R) <= TOINT(CINZAR+RUIDO)) and 
                (TOINT(CINZAG-RUIDO) <= TOINT(G) and TOINT(G) <= TOINT(CINZAG+RUIDO)) and
                (TOINT(CINZAB-RUIDO) <= TOINT(B) and TOINT(B) <= TOINT(CINZAB+RUIDO))):
                print("CINZA")
        elif(   (TOINT(CREMER-RUIDO) <= TOINT(R) and TOINT(R) <= TOINT(CREMER+RUIDO)) and 
                (TOINT(CREMEG-RUIDO) <= TOINT(G) and TOINT(G) <= TOINT(CREMEG+RUIDO)) and
                (TOINT(CREMEB-RUIDO) <= TOINT(B) and TOINT(B) <= TOINT(CREMEB+RUIDO))):
                print("CREME")
        elif(   (TOINT(PRETOR-RUIDO) <= TOINT(R) and TOINT(R) <= TOINT(PRETOR+RUIDO)) and
                (TOINT(PRETOG-RUIDO) <= TOINT(G) and TOINT(G) <= TOINT(PRETOG+RUIDO)) and
                (TOINT(PRETOB-RUIDO) <= TOINT(B) and TOINT(B) <= TOINT(PRETOB+RUIDO))):
                print("PRETO")
        elif(   (TOINT(VERDER-RUIDO) <= TOINT(R) and TOINT(R) <= TOINT(VERDER+RUIDO)) and
                (TOINT(VERDEG-RUIDO) <= TOINT(G) and TOINT(G) <= TOINT(VERDEG+RUIDO)) and
                (TOINT(VERDEB-RUIDO) <= TOINT(B) and TOINT(B) <= TOINT(VERDEB+RUIDO))):
                print("VERDE")
        elif(   (TOINT(VERMELHOR-RUIDO) <= TOINT(R) and TOINT(R) <= TOINT(VERMELHOR+RUIDO)) and 
                (TOINT(VERMELHOG-RUIDO) <= TOINT(G) and TOINT(G) <= TOINT(VERMELHOG+RUIDO)) and
                (TOINT(VERMELHOB-RUIDO) <= TOINT(B) and TOINT(B) <= TOINT(VERMELHOB+RUIDO))):
                print("VERMELHO")
        else:
            print("DESCONHECIDA")
except EOFError:
    pass