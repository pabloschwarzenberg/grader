import random
lista=["leptidoptero","casita","automovil"]
palabra=random.choice(lista)
def ocultar_letras(palabra, cantidad):
    l=len(palabra)
    palabra=list(palabra)
    t=1
    while(t<=cantidad):
        k=random.randint(0,l-1)
        if(palabra[k]=="-"):
            continue
        else:
            t=t+1        
            palabra[k]="-"
    palabra="".join(palabra)
    return(palabra)
def revisar_letra(palabra_secreta,palabra,letra):
    palabra=list(palabra)
    palabra_secreta=list(palabra_secreta)
    for i in range(0,len(palabra)):
        if(palabra_secreta[i]==letra):
            palabra[i]=letra
    palabra="".join(palabra)
    return(palabra)
if __name__ == "__main__":
    pass
         