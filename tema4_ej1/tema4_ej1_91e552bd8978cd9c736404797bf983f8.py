import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    palabra_oculta = "".join(letras_ocultas)
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_palabra_secreta = list(palabra_secreta)
    letras_mostradas = list(palabra_mostrada)
    for i in range(len(letras_palabra_secreta)):
        if letras_palabra_secreta[i] == letra:
            letras_mostradas[i] = letra
    nueva_palabra_mostrada = "".join(letras_mostradas)
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["elefante", "guitarra", "manzana", "computadora", "universidad"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, int(len(palabra_secreta)/2))
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinarla.")

    while intentos > 0:
        print("\nPalabra:", letras_mostradas)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        elif opcion == palabra_secreta:
            print("Felicidades, adivinaste la palabra!")
            break
        else:
            print("Palabra incorrecta. Sigue intentando.")

        intentos -= 1
        print("Te quedan", intentos, "intentos.")

    if intentos == 0:
        print("\nLo siento, has agotado tus intentos.")
        print("La palabra secreta era:", palabra_secreta)
         