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
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos_restantes = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes 7 intentos para adivinar la palabra.")

    while intentos_restantes > 0:
        print("\nPalabra actual:", palabra_mostrada)
        print("Intentos restantes:", intentos_restantes)

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion not in palabra_secreta:
                intentos_restantes -= 1
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
                break
            else:
                intentos_restantes -= 1

    if intentos_restantes == 0:
        print("\nLo siento, has agotado tus intentos.")
        print("La palabra secreta era:", palabra_secreta)
