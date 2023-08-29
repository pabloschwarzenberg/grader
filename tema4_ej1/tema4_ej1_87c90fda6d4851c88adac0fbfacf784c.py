from random import randint as rnd
def ocultar_letras(palabra, cantidad):

    old_palabra = palabra

    new_palabra = ""
    index = 0
    lista_hidden = []
    random_index = rnd(0, len(palabra) - 1)

    for i in range(cantidad):
        while random_index in lista_hidden:
            random_index = rnd(0, len(palabra) - 1)
        lista_hidden.append(random_index)

    for i in palabra:
        if index in lista_hidden:
            new_palabra += "_"
        else:
            new_palabra += i
        index += 1

    palabra_oculta = new_palabra

    return new_palabra


def revisar_letra(palabra_secreta, palabra, letra):
    palabrota = ""
    index = 0

    for i in palabra:
        if letra == i:
            palabrota += letra
        elif letra == palabra:
            return palabra
        else:
            palabrota += palabra_secreta[index]
        index += 1
    return palabrota
