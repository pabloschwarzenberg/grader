import random


def ocultar_letras(palabra, cantidad):
    i = 1
    a = len(palabra) - 1
    r = ""
    while i <= cantidad:
        u = random.randint(0, a)
        if str(u) not in r:
            palabra = palabra.replace(palabra[u], "_", 1)
            r += str(u)
            i += 1
    return palabra


def revisar_letra(palabra_secreta, palabra, letra):
    i = ""
    l = list(palabra)
    for a in range(0, (len(palabra_secreta))):
        if palabra[a] == "_":
            if palabra_secreta[a] == letra:
                l.pop(a)
                l.insert(a, letra)
    l = ''.join(l)
    return l
