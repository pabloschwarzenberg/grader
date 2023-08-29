from random import randint
def ocultar_letras(palabra, cantidad):
    palabra = "pianist"
    acumula = []
    palabra = list(palabra)
    while cantidad != 0:
        a = randint(1,len(palabra)-1)
        if a not in acumula:
            acumula.append(a)
            cantidad -= 1
            palabra[a] = "_"
    palabra = "".join(palabra)
    return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    a = list(palabra_secreta)
    palabra = list(palabra)
    if letra in a:
        b = palabra_secreta.find("-")
        palabra[b] = letra
    palabra = "".join(palabra)
    print(palabra)
    return palabra         