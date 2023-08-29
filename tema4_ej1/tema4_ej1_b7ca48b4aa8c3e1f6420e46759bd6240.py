from random import randint
def ocultar_letras(palabra, cantidad):
    palabra = "maquina"
    acumula = []
    palabra = list(palabra)
    while cantidad != 0:
        random = randint(1,len(palabra)-1)
        if random not in acumula:
         acumula.append(random)
         cantidad-=1
         palabra[random] = "_"
    palabra = "".join(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    random = list(palabra_secreta)
    palabra = list(palabra)
    if letra in random:
        Random = palabra_secreta.find("-")
        palabra[Random] = letra
    palabra = "".join(palabra)
    print(palabra)
    return palabra