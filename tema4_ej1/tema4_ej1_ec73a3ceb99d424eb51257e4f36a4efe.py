from random import randint
def ocultar_letras(palabra, cantidad):
    pala = "maquina"
    acu = []
    pala = list(palabra)
    while cantidad != 0:
        x = randint(1,len(pala)-1)
        if x not in acu:
         acu.append(x)
         cantidad-=1
         pala[x] = "_"
    pala = "".join(pala)
    return pala

def revisar_letra(palabra_secreta,pala,letra):
    x = list(palabra_secreta)
    pala = list(pala)
    if letra in x:
        y = palabra_secreta.find("-")
        pala[y] = letra
    pala = "".join(pala)
    print(pala)
    return pala