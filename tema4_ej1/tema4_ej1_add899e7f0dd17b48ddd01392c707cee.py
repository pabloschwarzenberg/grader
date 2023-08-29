import random

def ocultar_letras(palabra1,x):
    palabra=list(palabra1)
    cantidad=x
    y=len(palabra1)-1
    i=0
    
    while i<cantidad:
         numero = random.randint(0,y)
         palabra[numero]="_"
         i=i+1
    palabra="".join(palabra)
    return palabra

def revisar_letra(p,p_s,letra):
    i=0
    p_s=list(p_s)
    longitud=len(p)
    while i<longitud:
        if p_s[i]=="_":
            if p[i]==letra:
                p_s[i]=letra
        i=i+1
    p_s="".join(p_s)
    return p_s