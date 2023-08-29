from random import randint,choice

def ocultar_letras(palabra, cantidad):
    while cantidad > 0:
        pos = randint(0,len(palabra)-1)
        if palabra[pos]!="_":
            cantidad -= 1
            palabra = palabra[:pos]+"_"+palabra[pos+1:]
    return palabra

def revisar_letra(palabra_secreta, palabra, letra):
    for pos in range(len(palabra_secreta)):
        if palabra_secreta[pos]=="_" and palabra[pos]==letra:
            palabra_secreta = palabra_secreta[:pos]+letra+palabra_secreta[pos+1:]
    return palabra_secreta