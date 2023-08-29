import random

def ocultar_letras(palabra, cantidad):
    ocultada = list(palabra)
    indices = random.sample(range(len(palabra)), cantidad)
    for i in indices:
        ocultada[i] = "_"
    return "".join(ocultada)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "juego", "desafio"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    print("¡Bienvenido/a al juego de adivinar la palabra secreta!")
    print("Tienes 7 intentos para adivinar la palabra.")

    while intentos > 0:
        print("\nPalabra actual: {palabra_mostrada}")
        print("Intentos restantes: {intentos}")
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        elif len(opcion) > 1:
            if opcion == palabra_secreta:
                print("¡Felicidades! ¡Adivinaste la palabra!")
                break
            else:
                print("¡Incorrecto! Esa no es la palabra.")
                intentos -= 1

        if palabra_mostrada == palabra_secreta:
            print("¡Felicidades! ¡Adivinaste la palabra!")
            break

    if intentos == 0:
        print("¡Perdiste! Se te acabaron los intentos.")
    print("\nLa palabra secreta era: {palabra_secreta}")
