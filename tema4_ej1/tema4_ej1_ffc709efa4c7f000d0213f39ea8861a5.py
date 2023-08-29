from random import randint
def ocultar_letras(palabra, cantidad):
    palabra = "cazuela"
    acum = []
    palabra = list(palabra)
    while cantidad != 0:
        v = randint(1,len(palabra)-1)
        if v not in acum:
         acum.append(v)
         cantidad-=1
         palabra[v] = "_"
    palabra = "".join(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    v = list(palabra_secreta)
    palabra = list(palabra)
    if letra in v:
        a = palabra_secreta.find("-")
        palabra[a] = letra
    palabra = "".join(palabra)
    print(palabra)
    return palabra