from random import randint
def ocultar_letras(pal, cantidad):
    pal = "maquina"
    acumula = []
    pal = list(pal)
    while cantidad != 0:
        p = randint(1,len(pal)-1)
        if p not in acumula:
         acumula.append(p)
         cantidad-=1
         pal[p] = "_"
    pal = "".join(pal)
    return pal

def revisar_letra(palabra_secreta,pal,letra):
    p = list(palabra_secreta)
    pal = list(pal)
    if letra in p:
        y = palabra_secreta.find("-")
        pal[y] = letra
    pal = "".join(pal)
    print(pal)
    return pal