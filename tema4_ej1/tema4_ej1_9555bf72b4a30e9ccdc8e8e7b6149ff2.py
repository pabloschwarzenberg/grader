import random

def revisar_letra(palabra_secreta,palabra,letra):
    npal=""
    for l in range(len(palabra)):
        if palabra_secreta[l]=="_":
            if palabra[l]==letra:
                npal+=letra
            else:
                npal+="_"
        else:
            npal+=palabra[l]
    return npal
    
def ocultar_letras(palabra,cantidad):
    palabra_secreta=""
    oculto=random.sample(range(len(palabra)),cantidad)
    for l in range(len(palabra)):
        if l in oculto:
            palabra_secreta+="_"
        else:
            palabra_secreta+=palabra[l]
    return palabra_secreta

