import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = set()
    while len(letras_ocultas) < cantidad:
        indice = random.randint(0, len(palabra) - 1)
        letras_ocultas.add(indice)
    
    palabra_oculta = ""
    for i in range(len(palabra)):
        if i in letras_ocultas:
            palabra_oculta += "_"
        else:
            palabra_oculta += palabra[i]
    
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_oculta, letra):
    nueva_palabra_oculta = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_oculta += letra
        else:
            nueva_palabra_oculta += palabra_oculta[i]
    
    return nueva_palabra_oculta