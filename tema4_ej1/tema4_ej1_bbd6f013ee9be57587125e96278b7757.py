from random import randint


def ocultar_letras(palabra, cantidad):
    i = 0
    palabra = list(palabra)
    while i < cantidad:
        l = randint(0, len(palabra) - 1)
        if palabra[l] != "_":
            palabra[l] = "_"
        i += 1
    return "".join(palabra)


def revisar_letra(palabra_secreta, palabra, letra):
    print(palabra_secreta,palabra,letra)
    lu = []
    i = 0
    for l in palabra_secreta:
        if l == letra:
            lu.append(i)
        i += 1
    print(lu)
    palabra = list(palabra)
    for i in lu:
        palabra[i] = letra
    palabra = "".join(palabra)
    return palabra