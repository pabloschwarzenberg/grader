import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

def jugar_adivina_palabra():
    palabras_secretas = ["gato", "perro", "elefante", "tigre", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra!")
    print("La palabra contiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinarla.")

    while intentos > 0:
        print("\nPalabra:", palabra_mostrada)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) > 1:  # El jugador ingresó la palabra completa
            if opcion == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra.")
                return
            else:
                print("La palabra ingresada es incorrecta.")
                intentos -= 1
        else:  # El jugador ingresó una letra
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion not in palabra_secreta:
                print("La letra no está en la palabra.")
                intentos -= 1

    print("\n¡Perdiste! La palabra secreta era:", palabra_secreta)

if __name__ == "__main__":
    jugar_adivina_palabra()
