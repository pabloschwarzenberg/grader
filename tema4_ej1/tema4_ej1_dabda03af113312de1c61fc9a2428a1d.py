import random

def ocultar_letras(palabra, cantidad):
    ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        ocultas[indice] = "_"
    return "".join(ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "desarrollo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    while intentos > 0:
        print("Palabra:", palabra_mostrada)

        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(opcion) == 1:
            nueva_palabra = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if nueva_palabra == palabra_mostrada:
                print("La letra no está en la palabra secreta.")
                intentos -= 1
            else:
                palabra_mostrada = nueva_palabra
                if palabra_mostrada == palabra_secreta:
                    print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
                    break
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
                break
            else:
                print("La palabra no es correcta.")
                intentos -= 1

        print("Intentos restantes:", intentos)
        print()

    if intentos == 0:
        print("¡Lo siento! Has agotado todos tus intentos.")
        print("La palabra secreta era:", palabra_secreta)
