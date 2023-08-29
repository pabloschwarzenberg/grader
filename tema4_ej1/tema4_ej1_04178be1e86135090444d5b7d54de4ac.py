import random
def ocultar_letras(palabra, cantidad):
    palabra2 = list(palabra)
    posiciones = [] 
    while len(posiciones) != cantidad: 
        posicion = random.randint(0,len(palabra)-1)
        if posicion not in posiciones:
            posiciones.append(posicion)
    for posicion in posiciones:
        palabra2[posicion] = "_"
    return "".join(palabra2)

def revisar_letra(palabra_secreta, palabra, letra):
    palabra2 = list(palabra)
    for indice, letra_secreta in enumerate(palabra_secreta):
        if letra_secreta == letra:
            palabra2[indice] = letra_secreta
    return "".join(palabra2)  