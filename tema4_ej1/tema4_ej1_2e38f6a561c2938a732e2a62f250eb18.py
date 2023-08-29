from random import randint


def ocultar_letras(palabra, cantidad):
    palabra = list(palabra)
    cantidad_cambios = 0
    while cantidad_cambios < cantidad:
        random = randint(0, len(palabra) - 1)
        if palabra[random] == "_":
            continue
        palabra[random] = "_"
        cantidad_cambios = cantidad_cambios + 1
    palabra = "".join(palabra)
    return palabra


def revisar_letra(palabra_secreta, palabra, letra): #palabra secreta = palbra completa, palabra = palabra con guion bajo
    palabra = list(palabra)
    ekizde = 0
    lol = []
    if letra in palabra_secreta:
        for i in palabra_secreta:
            if i == letra:
                lol.append(ekizde)
            ekizde = ekizde + 1
    for i in lol:
        palabra[i] = letra
    palabra = "".join(palabra)
    return palabra
         