import random
palabras="lepidoptero"

def ocultar_letras(palabra,cantidad):
    i=0
    palabra_secreta=list(palabra)
    #numeros ya ocupados
    l=[]
    while i<cantidad:
        a=random.randint(0,len(palabra_secreta)-1)
        if a not in l:
            l.append(a)
            palabra_secreta[a]="_"
            i+=1
        else:
            i=i
    palabra_secreta_final="".join(palabra_secreta)
    return palabra_secreta_final

def revisar_letra(palabra,palabra_secreta,letra):
    palabra=list(palabras)
    palabra_secreta=list(palabra_secreta)
    i=0
    while i<len(palabra):
        if palabra[i]==letra:
            palabra_secreta[i]=letra
        i+=1
    palabra_final="".join(palabra_secreta)
    return palabra_final

if __name__ == "__main__":
    pass
         