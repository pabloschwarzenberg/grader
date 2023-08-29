import random
palabra = "berneri amoros gramsci".split()

def ocultar_letras(palabra,cantidad):
    palabra = list(palabra)
    for i in range(cantidad):
        posiciones = random.randint(1,len(palabra)) - 1
        if palabra[posiciones] == "_":
            posiciones = random.randint(1, len(palabra)) - 1
        palabra[posiciones] = "_"
    palabra = "".join(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    palabra = list(palabra)
    palabra_secreta = list(palabra_secreta)
    contador = 0
    numletra = palabra_secreta.count(letra)
    if numletra > 0:
        for i in palabra_secreta:
            if i == letra:
                palabra_secreta[contador] = contador
            contador += 1
        for p in range(len(palabra)):
            try:
                pos1 = palabra_secreta.index(p)
            except ValueError:
                continue
            pos1 = palabra_secreta.index(p)
            palabra[pos1] = letra
    palabrafinalizada = "".join(palabra)
    return palabrafinalizada

         