import random
def ocultar_letras(palabra,cantidad):
    while palabra.count("_") != cantidad:
        palabra = list(palabra)
        palabra[random.randint(0,len(palabra)-1)] = "_"
        palabra = "".join(palabra)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta = list(palabra_secreta)
    palabra = list(palabra)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra[i] = letra

    palabra = "".join(palabra)
    return palabra

if __name__ == "__main__":
    pass