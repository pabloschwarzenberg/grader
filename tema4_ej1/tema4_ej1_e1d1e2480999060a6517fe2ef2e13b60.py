import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["mono", "perro", "elefante", "koala", "hipopotamo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, len(palabra_secreta) // 2)
    intentos = 7

    print("¡Bienvenido al juego de adivinar palabras!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes 7 intentos para adivinarla.")

    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Intentos restantes:", intentos)

        opcion = input("Ingrese una letra o adivine la palabra completa: ").lower()

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
                break
            else:
                print("Lo siento, esa no es la palabra secreta.")

        intentos -= 1

    if intentos == 0:
        print("¡Se acabaron los intentos! La palabra secreta era:", palabra_secreta)


         