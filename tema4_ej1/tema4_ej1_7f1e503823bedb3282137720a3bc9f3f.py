import random

def escoger_palabra_secreta(lista_palabras):
    palabra_secreta = random.choice(lista_palabras)
    return palabra_secreta

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_mostrada[i] = letra
    return "".join(palabra_mostrada)

if __name__ == "__main__":
    lista_palabras = ["python", "programacion", "juego", "ordenador", "internet", "openai"]
    palabra_secreta = escoger_palabra_secreta(lista_palabras)
    cantidad_letras_ocultas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, cantidad_letras_ocultas)
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    while intentos > 0:
        print("\nPalabra mostrada:", palabra_mostrada)
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion not in palabra_secreta:
                intentos -= 1

        elif opcion == palabra_secreta:
            print("¡Felicitaciones! ¡Has adivinado la palabra secreta!")
            break

        else:
            print("¡Oops! No has adivinado la palabra secreta.")
            break

        if palabra_mostrada == palabra_secreta:
            print("¡Felicitaciones! ¡Has adivinado la palabra secreta!")
            break

        print("Intentos restantes:", intentos)

    if intentos == 0:
        print("¡Oh no! Has agotado tus intentos. La palabra secreta era:", palabra_secreta)
