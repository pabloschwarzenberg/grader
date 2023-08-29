import random

def ocultar_letras(palabra,cantidad):
    largo=len(palabra)-1
    palabra=list(palabra)
    a=0
    while a<cantidad:
        posicion=random.randint(0,largo)
        while palabra[posicion]=="_":
            posicion=random.randint(0,largo)
        palabra[posicion]="_"
        a+=1
    palabra="".join(palabra)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    largo=len(palabra_secreta)
    palabra_secreta=list(palabra_secreta)
    palabra=list(palabra)
    a=0
    while a<largo:
        if letra==palabra_secreta[a]:
            palabra[a]=letra
        a+=1
    palabra="".join(palabra)
    return palabra
if __name__ == "__main__":
    pass
         