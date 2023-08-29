from random import randint
palabra="lepidoptero"
def ocultar_letras(palabra, cantidad):
    palabra = list(palabra)
    lista=[]
    while cantidad != 0:
        x = randint(1,len(palabra)-1)
        if x not in lista:
         lista.append(x)
         palabra[x]="_"
         cantidad-=1
    palabra="".join(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    x=list(palabra_secreta)
    palabra= list(palabra)
    if letra in x:
        x=palabra_secreta.find("-")
        palabra[x]=letra
    palabra="".join(palabra)

    return palabra

if __name__ == "__main__":
    pass
         