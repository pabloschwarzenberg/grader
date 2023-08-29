import random

def ocultar_letras(palabra, cantidad):
    # Convertir la palabra en una lista de caracteres
    palabra_lista = list(palabra)

    # Obtener una lista aleatoria de índices para ocultar letras
    indices_ocultos = random.sample(range(len(palabra_lista)), cantidad)

    # Ocultar las letras en los índices seleccionados
    for indice in indices_ocultos:
        palabra_lista[indice] = "_"

    # Convertir la lista de caracteres de vuelta a una cadena
    palabra_oculta = "".join(palabra_lista)

    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    # Convertir la palabra secreta y la palabra mostrada en listas de caracteres
    palabra_secreta_lista = list(palabra_secreta)
    palabra_mostrada_lista = list(palabra_mostrada)

    # Revisar si la letra ingresada está en la palabra secreta
    for indice, caracter in enumerate(palabra_secreta_lista):
        if caracter == letra:
            palabra_mostrada_lista[indice] = letra

    # Convertir las listas de caracteres de vuelta a cadenas
    palabra_secreta_actualizada = "".join(palabra_secreta_lista)
    palabra_mostrada_actualizada = "".join(palabra_mostrada_lista)

    return palabra_mostrada_actualizada

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "python", "programacion", "computadora", "juego"]

    # Escoger una palabra secreta al azar
    palabra_secreta = random.choice(palabras_secretas)

    # Escoger aleatoriamente cuántas letras ocultar
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)

    # Ocultar las letras en la palabra secreta
    palabra_oculta = ocultar_letras(palabra_secreta, letras_ocultas)
    print("Palabra secreta:", palabra_oculta)

    while True:
        opcion = input("¿Deseas ingresar una letra (L) o arriesgarte a decir la palabra completa (P)? ")

        if opcion.upper() == "L":
            letra = input("Ingresa una letra: ")
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, letra)
            print("Palabra secreta:", palabra_oculta)
        elif opcion.upper() == "P":
            palabra_completa = input("Ingresa la palabra completa: ")

            if palabra_completa == palabra_secreta:
                print("¡Felicitaciones! Adivinaste la palabra secreta.")
            else:
                print("La palabra ingresada no es correcta. La palabra secreta era:", palabra_secreta)
            break
        else:
            print("Opción inválida. Ingresa 'L' para ingresar una letra o 'P' para arriesgarte a decir la palabra completa.")
