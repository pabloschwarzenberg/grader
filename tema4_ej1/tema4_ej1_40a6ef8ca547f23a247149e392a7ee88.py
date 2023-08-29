from random import randint
palabra="lepidoptero"
def ocultar_letras(palabra, cantidad):
    palabra = list(palabra)
    lista=[]
    while cantidad != 0:
        a = randint(1,len(palabra)-1)
        if a not in lista:
         lista.append(a)
         palabra[a]="_"
         cantidad-=1
    palabra="".join(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    a=list(palabra_secreta)
    palabra= list(palabra)
    if letra in a:
        x=palabra_secreta.find("-")
        palabra[x]=letra
    palabra="".join(palabra)

    return palabra
         