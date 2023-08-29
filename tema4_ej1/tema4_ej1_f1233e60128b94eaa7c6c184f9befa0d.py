def ocultar_letras(palabra,cantidad):
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
import random

def ocultar_letras(palabra, cantidad):
    # Convertir la palabra en una lista de caracteres
    palabra_lista = list(palabra)
    # Generar una lista con las posiciones aleatorias para ocultar letras
    posiciones_ocultas = random.sample(range(len(palabra)), cantidad)
    # Ocultar las letras en las posiciones seleccionadas
    for posicion in posiciones_ocultas:
        palabra_lista[posicion] = "_"
    # Convertir la lista de caracteres de nuevo a una cadena de texto
    palabra_oculta = "".join(palabra_lista)
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    # Convertir la palabra secreta y la palabra mostrada en listas de caracteres
    palabra_secreta_lista = list(palabra_secreta)
    palabra_mostrada_lista = list(palabra_mostrada)
    # Verificar si la letra ingresada está en la palabra secreta
    for i in range(len(palabra_secreta_lista)):
        if palabra_secreta_lista[i] == letra:
            palabra_mostrada_lista[i] = letra
    # Convertir las listas de caracteres de nuevo a cadenas de texto
    palabra_secreta_actualizada = "".join(palabra_secreta_lista)
    palabra_mostrada_actualizada = "".join(palabra_mostrada_lista)
    return palabra_mostrada_actualizada

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "elefante", "guitarra", "computadora", "programacion"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion in palabra_mostrada:
                print("La letra está en la palabra.")
            else:
                print("La letra no está en la palabra.")
        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! Has adivinado la palabra secreta.")
                break
            else:
                print("La palabra ingresada no es correcta.")

        intentos -= 1

    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)
      