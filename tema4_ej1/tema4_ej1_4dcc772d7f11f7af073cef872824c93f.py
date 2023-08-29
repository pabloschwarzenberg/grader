import random

def ocultar_letras(palabra, cantidad):
    for j in range(0, cantidad):
        a = True
        while a:
            i = random.randrange(0,len(palabra))
            if(palabra[i] != "_" or palabra == "_"*len(palabra)):
                palabra = palabra[:i]+"_"+palabra[i+1:]
                a = False
    return palabra

def revisar_letra(palabra_secreta, palabra, letra):
    if(palabra_secreta == letra):
        return letra
    for i in range(0,len(palabra_secreta)):
        if(palabra_secreta[i] == letra):
            palabra = palabra[:i]+letra+palabra[i+1:]
    return palabra


         