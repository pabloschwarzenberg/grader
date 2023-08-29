import random
def ocultar_letras(palabra, cantidad):
    xd = []
    contador = 0
    palabra_oculta = ""
    while contador < cantidad:
        i = random.randint(0, len(palabra)-1)
        if i not in xd:
            xd.append(i)
            contador = contador + 1
    contador = 0
    while len(palabra) > contador:
        if contador in xd:
            palabra_oculta = palabra_oculta + "_"
        else:
            palabra_oculta = palabra_oculta + palabra[contador]
        contador = contador + 1
    return palabra_oculta


def revisar_letra(palabra_secreta, palabra, letra):
    contador = 0
    palabra2 = ""
    while len(palabra_secreta) > contador:
        if letra == palabra_secreta[contador]:
            palabra2 = palabra2 + palabra_secreta[contador]
        else:
            palabra2 = palabra2 + palabra[contador]
        contador = contador + 1
    return palabra2