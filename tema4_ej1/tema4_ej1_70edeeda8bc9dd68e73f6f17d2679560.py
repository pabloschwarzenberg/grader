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
    palabras_secretas = ["python", "programacion", "juego", "adivinar", "palabra"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, int(len(palabra_secreta)/2))
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    while intentos > 0:
        print("Palabra:", letras_ocultas)

        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        opcion = opcion.lower()

        if len(opcion) == 1:
            letras_ocultas = revisar_letra(palabra_secreta, letras_ocultas, opcion)
            if opcion in palabra_secreta:
                print("¡Letra correcta!")
            else:
                print("Letra incorrecta.")
                intentos -= 1
        else:
            if opcion == palabra_secreta:
                print("¡Adivinaste la palabra!")
                break
            else:
                print("Palabra incorrecta.")
                intentos -= 1

        print("Intentos restantes:", intentos)
        print()

    if intentos == 0:
        print("¡Se te acabaron los intentos!")
        print("La palabra secreta era:", palabra_secreta)
      