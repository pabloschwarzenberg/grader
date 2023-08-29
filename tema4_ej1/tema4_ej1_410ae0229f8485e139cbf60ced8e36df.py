import random


def ocultar_letras(palabra,cantidad):
    P=list(palabra)
    palabra1=random.sample(P,cantidad)
    i=0
    while i<len(palabra1):
        palabra2=palabra.replace(palabra1[i],"_")
        i+=1
    return palabra2 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra


         