import random
def ocultar_letras(palabra, cantidad):
    string = ""
    pos=random.sample(range(len(palabra)),cantidad)

    for i in range(len(palabra)):
        if i in pos:
            string += "_"
        else:
            string += palabra[i]
    return string

def revisar_letra(palabra_secreta, palabra, letra):
    palabra_final = ""
    i=0
    while i < len(palabra_secreta):
        indice_s = palabra_secreta[i]
        indice_p = palabra[i]

        if indice_s == indice_p:
            palabra_final += indice_s
        elif indice_p == "_" and indice_s == letra:
            palabra_final += letra
        elif indice_p == "_" and indice_s != letra:
            palabra_final += "_"
        i += 1

    if palabra_secreta == palabra_final:
        return palabra_secreta
    else:
        return palabra_final
