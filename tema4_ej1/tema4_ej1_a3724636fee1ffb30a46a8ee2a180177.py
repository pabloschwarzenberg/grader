from random import randint
palabrasSecretas = ["lepidoptero", "verdad", "adios", "gato", "perro", "programacion"]
palabra = palabrasSecretas[randint(0, len(palabrasSecretas)) - 1]

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
    contador = 0
    while (contador < len(palabra)):
        while (letra == palabra[contador]):
            palabra_secreta = str(palabra_secreta[:contador]) + str(letra) + str(palabra_secreta[contador + 1:])
            break
        contador += 1
    if (letra == palabra):
        palabra_secreta = palabra
    return palabra_secreta
   




palabra_secreta = (ocultar_letras(palabra, 4))
print(palabra_secreta)
print(revisar_letra(palabra_secreta , palabra, str(input("Ingrese una letra: "))))

