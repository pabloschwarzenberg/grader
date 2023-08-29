from random import randint
def ocultar_letras(palabra, cantidad):
    palabra = "camioneta"
    acumula = []
    palabra = list(palabra)
    while cantidad != 0:
        e = randint(1,len(palabra)-1)
        if e not in acumula:
         acumula.append(e)
         cantidad-=1
         palabra[e] = "_"
    palabra = "".join(palabra)
    return palabra
   
def revisar_letra(palabra_secreta,palabra,letra):
    e = list(palabra_secreta)
    palabra = list(palabra)
    if letra in e:
        o = palabra_secreta.find("-")
        palabra[o] = letra
    palabra = "".join(palabra)
    print(palabra)
    return palabra