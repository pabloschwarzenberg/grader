import random


def ocultar_letras(palabra, cantidad):
    largo = len(palabra)
    cantidad
    if cantidad <= largo:
        while cantidad != 0:
            especifico = random.randrange(0, largo)
            palabra[especifico]
            letra = palabra[especifico]
            if letra != "_":
                palabra = palabra.replace(str(letra), "_", 1)
                cantidad = cantidad - 1

        return palabra


def revisar_letra(palabra_secreta,palabra,letra):
    vidas=7
    ac=len(palabra_secreta)
    for i in range(ac):
            if letra in palabra_secreta[i]:
                palabra= palabra[:i] + palabra_secreta[i] + palabra[i+1:]
    return palabra

    if letra not in palabra_secreta:
            vidas=vidas-1
            return palabra
    if palabra_secreta == palabra:
            return palabra