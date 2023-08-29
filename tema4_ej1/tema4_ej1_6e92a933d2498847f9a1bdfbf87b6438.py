import random
def ocultar_letras(palabra, cantidad):
    muestra = random.sample(range(len(palabra)), cantidad)
    string = ''
    for i in range(len(palabra)):
        if i in muestra:
            string += '_'
        else:
            string += palabra[i]
    return(string)
def revisar_letra(palabra_secreta, palabra, letra):
    string = ''
    for i in range(len(palabra_secreta)):
        if letra in palabra_secreta[i]:
            string += letra
        else:
            string += palabra[i]
    return string