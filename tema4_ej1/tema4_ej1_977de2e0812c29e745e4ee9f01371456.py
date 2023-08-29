import random

def escoger_palabra_secreta(palabras):
    return random.choice(palabras)

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)

    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"

    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)

    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada[i] = letra

    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "elefante", "programacion", "banana", "computadora"]
    palabra_secreta = escoger_palabra_secreta(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta.")
    print("La palabra tiene", len(palabra_secreta), "letras y se han ocultado", letras_ocultas, "letras.")

    while intentos > 0:
        print("Palabra actual:", palabra_mostrada)
        print("Intentos restantes:", intentos)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
                break
            else:
                print("La palabra ingresada es incorrecta.")

        if palabra_mostrada == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break

        intentos -= 1

    if intentos == 0:
        print("Has agotado tus intentos. La palabra secreta era:", palabra_secreta)

         