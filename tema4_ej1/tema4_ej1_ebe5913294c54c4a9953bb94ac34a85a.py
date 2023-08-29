from random import randint

def ocultar_letras(palabra, cantidad):
    i = 0
    palabra = list(palabra)
    while i < cantidad:
        cambio = randint(0, 1)  # 0 es no cambiar, 1 es cambiar
        posicion = randint(0, len(palabra) - 1)
        if palabra[posicion] == "_":
            continue
        if cambio == 1:
            palabra[posicion] = "_"
            i += 1
    palabra = "".join(palabra)
    return palabra
    
def revisar_letra(palabra_secreta, palabra, letra):
    palabra = list(palabra)
    for i in range(0, len(palabra)):
        if letra == palabra_secreta[i]:
            palabra[i] = letra
    palabra= "".join(palabra)
    return palabra