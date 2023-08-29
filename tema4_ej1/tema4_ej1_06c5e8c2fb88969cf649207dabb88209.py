import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    posiciones_ocultas = random.sample(range(len(palabra)), cantidad)
    for pos in posiciones_ocultas:
        letras_ocultas[pos] = "_"
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
    palabras_secretas = ["python", "programacion", "desafio", "computadora", "teclado"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, int(len(palabra_secreta)/2))
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    while intentos > 0:
        print("\nPalabra:", letras_ocultas)
        print("Intentos restantes:", intentos)

        opcion = input("Ingresa una letra o arriesga la palabra completa: ")

        if len(opcion) > 1:
            if opcion == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra secreta:", palabra_secreta)
                break
            else:
                print("Lo siento, esa no es la palabra secreta.")
                intentos -= 1
        else:
            letras_ocultas = revisar_letra(palabra_secreta, letras_ocultas, opcion)
            if opcion not in palabra_secreta:
                print("La letra no está en la palabra secreta.")
                intentos -= 1
            else:
                print("¡Bien hecho! La letra está en la palabra secreta.")

    if intentos == 0:
        print("\n¡Perdiste! La palabra secreta era:", palabra_secreta)
