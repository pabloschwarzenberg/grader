from random import sample

def ocultar_letras(palabra,cantidad):
    L = list(palabra)
    sL = sample(range(len(palabra)),cantidad)
    for i in sL:
        L[i] = "_"
    palabra = "".join(L)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    L = list(palabra)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            L[i] = letra
    palabra = "".join(L)
    return palabra