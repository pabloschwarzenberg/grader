import random

# Lista de palabras secretas
palabras_secretas = ["python", "programacion", "computadora", "juego", "desarrollo"]

def ocultar_letras(palabra, cantidad):
    # Convierte la palabra en una lista para poder modificarla
    lista_palabra = list(palabra)
    # Obtiene las posiciones donde se ocultarán las letras
    posiciones_ocultas = random.sample(range(len(palabra)), cantidad)
    # Reemplaza las letras en las posiciones ocultas por "_"
    for posicion in posiciones_ocultas:
        lista_palabra[posicion] = "_"
    # Convierte la lista de nuevo a una cadena
    palabra_oculta = "".join(lista_palabra)
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    # Convierte las palabras en listas para poder modificarlas
    lista_secreta = list(palabra_secreta)
    lista_mostrada = list(palabra_mostrada)
    # Reemplaza la letra en todas las posiciones que aparece en la palabra secreta
    for i in range(len(lista_secreta)):
        if lista_secreta[i] == letra:
            lista_mostrada[i] = letra
    # Convierte las listas de nuevo a cadenas
    palabra_secreta_actualizada = "".join(lista_secreta)
    palabra_mostrada_actualizada = "".join(lista_mostrada)
    return palabra_mostrada_actualizada

if __name__ == "__main__":
    # Escoge una palabra secreta aleatoriamente
    palabra_secreta = random.choice(palabras_secretas)
    # Oculta algunas letras de la palabra secreta
    palabra_mostrada = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta) - 1))
    intentos = 7

    while intentos > 0:
        print("Palabra: ", palabra_mostrada)
        print("Intentos restantes:", intentos)

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if opcion == palabra_secreta:
            print("¡Adivinaste la palabra! La palabra era:", palabra_secreta)
            break

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if palabra_mostrada == palabra_secreta:
                print("¡Adivinaste la palabra! La palabra era:", palabra_secreta)
                break
            elif opcion not in palabra_secreta:
                intentos -= 1
                print("La letra no está en la palabra secreta.")
        else:
            intentos -= 1
            print("¡Intento fallido!")

    if intentos == 0:
        print("No adivinaste la palabra. La palabra era:", palabra_secreta)