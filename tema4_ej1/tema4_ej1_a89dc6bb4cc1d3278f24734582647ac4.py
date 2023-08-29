import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "juego", "inteligencia"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    print("Bienvenido a 'Adivina la palabra'")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        elif opcion == palabra_secreta:
            palabra_mostrada = opcion
            break
        else:
            print("¡Ups! No es la palabra correcta.")
            intentos -= 1

        if palabra_mostrada == palabra_secreta:
            break

    if palabra_mostrada == palabra_secreta:
        print("¡Felicidades! Has adivinado la palabra:", palabra_mostrada)
    else:
        print("¡Oh no! Te has quedado sin intentos. La palabra era:", palabra_secreta)
