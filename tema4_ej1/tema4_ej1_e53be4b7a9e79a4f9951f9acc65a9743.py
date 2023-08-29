import random
from random import sample
def ocultar_letras(palabra,cantidad):
    x = sample(range(0, len(palabra)),cantidad)
    for i in x:
        palabra = palabra.replace(palabra[i], '_', 1)       
    return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    k=-1
    if letra in palabra_secreta:
        for caracter in palabra_secreta:
            k+=1
            if caracter == letra:
                fin = len(palabra)
                palabra = palabra[0:k] + letra + palabra[k+1:fin]
        return palabra