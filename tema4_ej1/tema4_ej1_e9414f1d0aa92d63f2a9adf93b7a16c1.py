import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)

    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"

    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""

    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]

    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "loro"]
    palabra_secreta = random.choice(palabras_secretas)

    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))

    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("Tienes 7 intentos para adivinar la palabra.")

    while intentos > 0:
        print("\nPalabra:", letras_mostradas)
        print("Intentos restantes:", intentos)

        respuesta = input("Ingresa una letra o arriésgate con la palabra completa: ")

        if len(respuesta) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, respuesta)
            if respuesta in palabra_secreta:
                print("¡Bien hecho! La letra está en la palabra.")
            else:
                print("No está la letra en la palabra. Sigue intentándolo.")
        else:
            if respuesta == palabra_secreta:
                print("¡Felicitaciones! Adivinaste la palabra.")
                break
            else:
                print("Esa no es la palabra correcta. Sigue intentándolo.")

        intentos -= 1

    if intentos == 0:
        print("\n¡Agotaste tus intentos! La palabra secreta era:", palabra_secreta)
