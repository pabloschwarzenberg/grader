import random

def ocultar_letras(palabra, cantidad):
    palabra_ocultada = ""
    letras = random.sample(range(len(palabra)),cantidad)
    for idx in range(len(palabra)):
        if idx not in letras:
            palabra_ocultada += palabra[idx]
        else:
            palabra_ocultada += "_"
    palabra = palabra_ocultada
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    for idx in range(len(palabra_secreta)):
        if palabra_secreta[idx] == letra:
            palabra = palabra [:idx] + letra + palabra[idx+1:]
    return palabra