# Importaciones
from random import randint

def ocultar_letras(palabra, cantidad):
    palabra = list(palabra)
    ocultacion = []
    while cantidad > 0:
        i = randint(1, len(palabra)-1)
        if i not in ocultacion:
            ocultacion.append(i)
            palabra[i] = "_"
            cantidad -= 1
    palabra = "".join(palabra)
    return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    palabra = list(palabra)
    for letra in list(palabra_secreta):
        x = palabra_secreta.find("_")
        palabra[x] = letra
    palabra = "".join(palabra)
    return palabra