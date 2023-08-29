import random
from random import randint


def PalabrasSecretas(Palabras):
    palabra = random.choice(Palabras)
    return palabra

def ocultar_letras(palabra, cantidad):
    palabra_secreta = palabra
    counter = 0
    while (cantidad > counter):
        index = randint(0, len(palabra_secreta) - 1)
        while (palabra_secreta[index] == "_"):
            index = randint(0, len(palabra_secreta) - 1)
        palabra_secreta = str(palabra_secreta[:index]) + "_" + str(palabra_secreta[index + 1:])
        counter += 1
    return palabra_secreta

def revisar_letra(palabra_secreta, palabra, letra):
    counter = 0
    while (counter < len(palabra_secreta)):
        if (letra == palabra[counter]):
            palabra_secreta = str(palabra_secreta[:counter]) + str(letra) + str(palabra_secreta[counter + 1:])
        counter += 1
    if (letra == palabra):
        palabra_secreta = palabra
    return palabra_secreta

lista = ["lepidoptero", "verdad", "adios", "gato", "perro", "programacion"]
palabra = PalabrasSecretas(lista)
PalabrasSecreta = ocultar_letras(palabra, 4)
if __name__ == "__main__":
 print(PalabrasSecreta)
 print(revisar_letra(PalabrasSecreta, palabra, str(input("ingrese una letra: "))))