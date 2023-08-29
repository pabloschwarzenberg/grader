from random import randint
def ocultar_letras(P, C):
    P = "maquina"
    acumula = []
    P = list(P)
    while C != 0:
        x = randint(1,len(P)-1)
        if x not in acumula:
         acumula.append(x)
         C-=1
         P[x] = "_"
    P = "".join(P)
    return P

def revisar_letra(P_secreta,P,letra):
    x = list(P_secreta)
    P = list(P)
    if letra in x:
        y = P_secreta.find("-")
        P[y] = letra
    P = "".join(P)
    print(P)
    return P