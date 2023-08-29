import random

def ocultar_letras(palabra, cantidad):
    palabra_oculta = list(palabra)
    for i in range(cantidad):
        indice = random.randint(0, len(palabra_oculta)-1)
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra
