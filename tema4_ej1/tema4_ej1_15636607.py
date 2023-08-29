import random

def ocultar_letras(palabra,cantidad):
    letras=len(palabra)
    contador=0
    for i in range(0,cantidad):
        r=random.randint(1,letras)
        r2=r-1
        palabra=palabra[:r2]+"_"+palabra[r2+1:]
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    for i in range(0,len(palabra_secreta)):
        if letra==palabra_secreta[i]:
            a=palabra[:i]+letra+palabra[i+1:]
    return a

if __name__ == "__main__":
    pass