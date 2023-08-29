from random import randint

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
    if (letra == palabra_secreta):
        return letra
    while (counter < len(palabra)):
        if (letra == palabra_secreta[counter]):
            palabra = str(palabra[:counter]) + str(letra) + str(palabra[counter + 1:])
        counter += 1
    return palabra

if __name__ == "__main__":
  palabrasSecretas = ["lepidoptero", "verdad", "adios", "gato", "perro", "programacion"]
  palabra_secreta = palabrasSecretas[randint(0, len(palabrasSecretas)- 1)]
  palabra = (ocultar_letras(palabra_secreta, 4))
  while("_" in palabra):
    palabra = revisar_letra(palabra_secreta, palabra, str(input(" ingrese una letra: ")))