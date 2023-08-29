import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    nueva_palabra = ""
    for i, letra in enumerate(palabra):
        if i in letras_ocultas:
            nueva_palabra += "_"
        else:
            nueva_palabra += letra
    return nueva_palabra

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "internet", "teclado"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinarla.")
    print("¡Buena suerte!\n")

    while intentos > 0:
        print("Palabra oculta:", palabra_oculta)
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) > 1:
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
            else:
                print("Lo siento, esa no es la palabra secreta.")
            break

        palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)

        if palabra_oculta == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break

        intentos -= 1
        print("Incorrecto. Te quedan", intentos, "intentos.\n")

    if intentos == 0:
        print("Lo siento, has agotado todos tus intentos. La palabra secreta era:", palabra_secreta)
