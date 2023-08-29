import random

def ocultar_letras(palabra, cantidad):
    ocultada = list(palabra)
    indices_ocultar = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultar:
        ocultada[indice] = "_"
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
    palabras_secretas = ["python", "programacion", "computadora", "juego", "adivinar"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta)-1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    print("Bienvenido a Adivina la Palabra!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    while intentos > 0:
        print("Palabra:", palabra_mostrada)

        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion in palabra_secreta:
                print("¡Correcto! La letra", opcion, "está en la palabra.")
            else:
                print("La letra", opcion, "no está en la palabra.")
        elif opcion == palabra_secreta:
            print("¡Felicitaciones! Adivinaste la palabra.")
            break
        else:
            print("La palabra ingresada no es correcta.")

        intentos -= 1
        print("Intentos restantes:", intentos)
        print("-------------------")

    if intentos == 0:
        print("Has agotado tus intentos. La palabra secreta era:", palabra_secreta)
