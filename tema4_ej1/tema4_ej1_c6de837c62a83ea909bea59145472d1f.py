import random
def ocultar_letras(palabra, cantidad):
    a = 0
    palabra = list(palabra)
    palabraN = ''
    while a < cantidad:
        num = random.randint(0, len(palabra) - 1)
        if palabra[num] != '_':
            palabra[num] = '_'
            a += 1
        else:
            pass
    for a in palabra:
        palabraN += a
    return palabraN


def revisar_letra(palabra, palabra_secreta, letra):
    a = 0
    palabraF = ''
    palabra_secreta = list(palabra_secreta)
    palabra = list(palabra)
    while a < len(palabra):
        if letra == palabra[a]:
            palabra_secreta[a] = letra
            a += 1
        else:
            a += 1

    for z in palabra_secreta:
        palabraF += z
    palabraF.strip(' ')
    return palabraF