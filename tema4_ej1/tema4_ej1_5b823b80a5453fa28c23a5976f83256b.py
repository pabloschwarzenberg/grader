from random import randint

def ocultar_letras(palabra,cantidad):
    i = 0
    lista_palabra = list(palabra)
    while True:
        numeroRandom2 = randint(0, len(palabra)-1)
        if lista_palabra[numeroRandom2] != "_":
            lista_palabra[numeroRandom2] = "_"
            i += 1
        if i == cantidad:
            break

    palabra = "".join(lista_palabra)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    lista_palabra = list(palabra_secreta)
    for i in range(len(lista_palabra)):
        if palabra_secreta[i] == "_" and palabra[i] == letra:
            lista_palabra[i] = letra

    nueva_palabra = "".join(lista_palabra)
    return nueva_palabra

if __name__ == "__main__":
    pass