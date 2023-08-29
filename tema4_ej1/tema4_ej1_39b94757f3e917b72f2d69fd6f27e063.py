from random import randint
def ocultar_letras(palabra, cantidad):
    palabra = "arboles"
    Queda = []
    palabra = list(palabra)
    while cantidad != 0:
        i = randint(1,len(palabra)-1)
        if i not in Queda:
         Queda.append(i)
         cantidad-=1
         palabra[i] = "_"
    palabra = "".join(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    i = list(palabra_secreta)
    palabra = list(palabra)
    if letra in i:
        i2 = palabra_secreta.find("-")
        palabra[i2] = letra
    palabra = "".join(palabra)
    print(palabra)
    return palabra