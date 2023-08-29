import random
def ocultar_letras(palabra, cantidad):
    palabra_lista = list(palabra)
    n = 0
    while n < cantidad:
        x = random.randint(0, len(palabra_lista)-1)
        if palabra_lista[int(x)] != "_":
            palabra_lista[int(x)] = "_"
            n += 1
    return "".join(palabra_lista)


def revisar_letra(palabra_secreta, palabra, letra):
    palabra_secreta = list(palabra_secreta)
    palabra = list(palabra)
    letra = list(letra)
    palabra_revisada = list(palabra)
    for i in range(0, len(palabra_secreta)):
        if palabra_secreta[i] == letra[0] and palabra[i] == "_":
            palabra_revisada[i] = letra[0]
    if palabra == palabra_revisada:
        return "No existe esa letra en la palabra."
    else:
        return "".join(palabra_revisada)
