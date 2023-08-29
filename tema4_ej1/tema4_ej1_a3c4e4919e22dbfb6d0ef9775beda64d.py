from random import randint
def ocultar_letras(palabra, cant):
    palabra = "maquina"
    acumula = []
    palabra = list(palabra)
    while cant != 0:
        x = randint(1,len(palabra)-1)
        if x not in acumula:
         acumula.append(x)
         cant-=1
         palabra[x] = "_"
    palabra = "".join(palabra)
    return palabra

def revisar_letra(palabraSecreta,palabra,letra):
    x = list(palabraSecreta)
    palabra = list(palabra)
    if letra in x:
        y = palabraSecreta.find("-")
        palabra[y] = letra
    palabra = "".join(palabra)
    print(palabra)
    return palabra