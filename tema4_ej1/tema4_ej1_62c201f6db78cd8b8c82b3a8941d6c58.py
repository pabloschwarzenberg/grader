import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for i in letras_ocultas:
        palabra_oculta[i] = '_'
    return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra[i] = letra
    return ''.join(nueva_palabra)

def juego_adivina_palabra():
    palabras_secretas = ["python", "programacion", "computadora", "inteligencia", "algoritmo", "robotica", "inteligente", "tecnologia"]
    palabra_secreta = random.choice(palabras_secretas)

    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)

    intentos = 7

    print("Bienvenido al juego de Adivina la palabra.")
    print("Tienes hasta 7 intentos para adivinar la palabra secreta.")
    print("La palabra contiene {} letras y algunas de ellas están ocultas.".format(len(palabra_secreta)))

    while intentos > 0:
        print("\nPalabra actual: {}".format(palabra_mostrada))
        intento = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(intento) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, intento)
            if intento in palabra_secreta:
                print("¡Muy bien! La letra '{}' está en la palabra.".format(intento))
            else:
                intentos -= 1
                print("La letra '{}' no está en la palabra. Te quedan {} intentos.".format(intento, intentos))
        else:
            if intento == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
                return
            else:
                intentos -= 1
                print("La palabra ingresada no es correcta. Te quedan {} intentos.".format(intentos))

    print("\n¡Lo siento! Has agotado tus intentos. La palabra secreta era: '{}'".format(palabra_secreta))

if __name__ == "__main__":
    juego_adivina_palabra()
