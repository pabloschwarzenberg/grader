from random import randint
def ocultar_letras(palabra, cantidad):
    palabra = "informe"
    a = []
    palabra = list(palabra)
    while (cantidad != 0):
        i = randint(1,len(palabra)-1)
        if i not in a:
            a.append(i)
            cantidad -= 1
            palabra[i] = "_"
    palabra = "".join(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    i = list(palabra_secreta)
    palabra = list(palabra)
    if (letra in i):
        j = palabra_secreta.find("-")
        palabra[j] = letra
    palabra = "".join(palabra)
    print(palabra)
    return palabra