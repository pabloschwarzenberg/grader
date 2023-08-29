import random

def ocultar_letras(palabra, cantidad):
    lista_palabra = []
    posicion = random.sample(range(0, len(palabra)), cantidad)
    nueva_palabra = ""

    posicion.sort()

    for n in range(len(palabra)):
        lista_palabra.append(palabra[n])

    for n in range(cantidad):
        lista_palabra[posicion[n]] = "_"

    for n in lista_palabra:
        nueva_palabra += n

    return nueva_palabra


def revisar_letra(palabra_secreta, palabra, letra):
    lista_palabra = []
    lista_palabra_sec = []
    nueva_palabra = ""

   

    for n in range(len(palabra_secreta)):
        lista_palabra_sec.append(palabra_secreta[n])

    for n in range(len(palabra)):
        lista_palabra.append(palabra[n])

    indice = 0
    for n in lista_palabra_sec:
        if letra == n:
            lista_palabra[indice] = letra
        indice += 1

    for n in lista_palabra:
        nueva_palabra += n

    return nueva_palabra

if __name__ == "__main__":
    pass
         