import random

def ocultar_letras(palabra, cantidad):
    letra_oculta = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = ""
    for i in range(len(palabra)):
        if i in letra_oculta:
            palabra_oculta += "_"
        else:
            palabra_oculta += palabra[i]
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra, letra):
    palabra_actu = ''
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_actu += letra
        else:
            palabra_actu += palabra[i]
    return palabra_actu

