def ocultar_letras(palabra, cantidad):
    import random
    for x in range(cantidad):
        pos = random.randint(1, len(palabra)-1)
        palabra = palabra[:pos] + "_" + palabra[pos + 1:]
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
         