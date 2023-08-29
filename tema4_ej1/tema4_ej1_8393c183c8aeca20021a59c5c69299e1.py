from random import randint
def ocultar_letras(palabra, cantidad):
    palabra = "maquina"
    acumula = []
    palabra = list(palabra)
    while cantidad != 0:
        p = randint(1,len(palabra)-1)
        if p not in acumula:
         acumula.append(p)
         cantidad-=1
         palabra[p] = "_"
    palabra = "".join(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    p = list(palabra_secreta)
    palabra = list(palabra)
    if letra in p:
        y = palabra_secreta.find("-")
        palabra[y] = letra
    palabra = "".join(palabra)
    print(palabra)
    return palabra