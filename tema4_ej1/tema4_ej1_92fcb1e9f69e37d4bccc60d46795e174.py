from random import randint
palabrasSecretas = ["lepidoptero", "verdad", "adios", "gato", "perro", "programacion"]
palabra = palabrasSecretas[randint(0, len(palabrasSecretas)- 1)]

def ocultar_letras(palabra, cantidad):
    palabra_secreta = palabra
    contador = 0
    while (cantidad > contador):
        index = randint(0, len(palabra_secreta) - 1)
        while (palabra_secreta[index] == "_"):
            index = randint(0, len(palabra_secreta) - 1)
        palabra_secreta = str(palabra_secreta[:index]) + "_" + str(palabra_secreta[index + 1:])
        contador += 1
    return palabra_secreta

def revisar_letra(palabra_secreta, palabra, letra):
    counter = 0
    while (counter < len(palabra)):
        if (letra == palabra[counter]):
            palabra_secreta = str(palabra_secreta[:counter]) + str(letra) + str(palabra_secreta[counter + 1:])
        counter += 1
    if (letra == palabra):
        palabra_secreta = palabra
    print(palabra_secreta)
    return palabra_secreta