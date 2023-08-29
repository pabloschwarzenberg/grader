import random
def ocultar_letras(palabra, cantidad):
    posiciones = []
    lst = list(palabra)
    for i in range(cantidad):
        x = random.choice(range(len(palabra)))
        while x in posiciones:
            x = random.choice(range(len(palabra)))
        posiciones.append(x)
    for i in posiciones:
        lst[i] = '_'
    return ''.join(lst)


def revisar_letra(palabra_secreta, palabra, letra):
    posiciones = []
    for i in range(len(palabra_secreta)):
        if letra == palabra_secreta[i]:
            posiciones.append(i)
    palabra = list(palabra)
    for i in posiciones:
        palabra[i] = palabra_secreta[i]
    return ''.join(palabra)

if __name__ == "__main__":
    pass
         