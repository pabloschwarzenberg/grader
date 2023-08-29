import random
palabra = "perro whatsapp google twitch discor phyton hora titulos"


def ocultar_letras(palabra, cantidad):
    palabra = list(palabra)
    for p in range(cantidad):
        lugar = (random.randint(1, len(palabra))) - 1
        while palabra[lugar] == "_":
            lugar = (random.randint(1, len(palabra))) - 1
        if palabra[lugar] != "_":
            palabra[lugar] = "_"
    palabra = "".join(palabra)
    return palabra


def revisar_letra(palabra_secreta, palabra, letra):
    palabra_secreta = list(palabra_secreta)
    placeholder = palabra_secreta
    palabra = list(palabra)
    cantidad = palabra_secreta.count(letra)
    if cantidad > 0:
        for p in range(cantidad):
            pos = placeholder.index(letra)
            placeholder[pos] = p
        for i in range(cantidad):
            pos1 = placeholder.index(i)
            palabra[pos1] = letra
    palabra = "".join(palabra)
    return palabra
