import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
    palabra_actualizada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_actualizada += letra
        else:
            palabra_actualizada += palabra[i]
    return palabra_actualizada

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta))
    palabra_oculta = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")

    while intentos > 0:
        print("Palabra:", palabra_oculta)
        print("Intentos restantes:", intentos)
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)
        elif opcion == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break

        intentos -= 1

    if palabra_oculta == palabra_secreta:
        print("¡Felicidades! Has adivinado la palabra secreta.")
    else:
        print("Lo siento, se acabaron los intentos. La palabra secreta era:", palabra_secreta)
