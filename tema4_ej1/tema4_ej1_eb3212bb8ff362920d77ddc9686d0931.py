import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = list(palabra)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra[indice] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "juego", "adivinar"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("¡Bienvenido al juego Adivina la Palabra!")
    print("Tienes 7 intentos para adivinar la palabra secreta.")
    print("Palabra a adivinar: {palabra_oculta}")

    while intentos > 0:
        if "_" not in palabra_oculta:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break

        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(letra) == 1:
            nueva_palabra = revisar_letra(palabra_secreta, palabra_oculta, letra)
            if nueva_palabra == palabra_oculta:
                intentos -= 1
                print("La letra '{letra}' no está en la palabra secreta. Intentos restantes: {intentos}")
            else:
                palabra_oculta = nueva_palabra
                print("Palabra actualizada: {palabra_oculta}")
        else:
            if letra == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra!")
                break
            else:
                intentos -= 1
                print("La palabra '{letra}' no es la correcta. Intentos restantes: {intentos}")

    if intentos == 0:
        print("¡Lo siento! Has agotado tus intentos. La palabra secreta era:", palabra_secreta)