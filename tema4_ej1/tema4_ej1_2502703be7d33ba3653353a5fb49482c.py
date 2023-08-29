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
    palabras_secretas = ["python", "programacion", "computadora", "algoritmo", "desarrollo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras y algunas están ocultas.")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    while intentos > 0:
        print("Palabra:", palabra_mostrada)

        eleccion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(eleccion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, eleccion)
            if eleccion in palabra_secreta:
                print("¡Letra encontrada!")
            else:
                intentos -= 1
                print("Letra incorrecta. Te quedan", intentos, "intentos.")
        else:
            if eleccion == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra secreta!")
                break
            else:
                intentos -= 1
                print("Palabra incorrecta. Te quedan", intentos, "intentos.")

        if palabra_mostrada == palabra_secreta:
            print("¡Felicidades! ¡Has adivinado la palabra secreta!")
            break

        if intentos == 0:
            print("¡Has agotado todos tus intentos! La palabra secreta era:", palabra_secreta)
