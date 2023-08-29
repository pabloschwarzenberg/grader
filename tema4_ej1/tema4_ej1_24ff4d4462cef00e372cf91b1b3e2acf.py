from random import randint
palabra="lepidoptero"
def ocultarletras(palabra, cantidad):
    palabra = list(palabra)
    l=[]
    while cantidad != 0:
        f = randint(1,len(palabra)-1)
        if f not in l:
         l.append(f)
         palabra[f]=""
    palabra="".join(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    y=list(palabra_secreta)
    palabra= list(palabra)
    if letra in y:
        x=palabra_secreta.find("-")
        palabra[x]=letra
    palabra="".join(palabra)
    return palabra

if __name__ == "__main__":
    pass