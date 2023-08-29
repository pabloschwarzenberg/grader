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
    palabras_secretas = ["elefante", "guitarra", "computadora", "sol", "galleta"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, int(len(palabra_secreta) / 2))
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    while intentos > 0:
        print("Palabra actual:", letras_mostradas)
        print("Intentos restantes:", intentos)
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if opcion not in palabra_secreta:
                intentos -= 1
        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! ¡Has adivinado la palabra secreta!")
                break
            else:
                print("¡Oh no! La palabra ingresada no es correcta.")
                intentos -= 1

        if letras_mostradas == palabra_secreta:
            print("¡Felicitaciones! ¡Has adivinado la palabra secreta!")
            break

    if intentos == 0:
        print("¡Oh no! Te has quedado sin intentos. La palabra secreta era:", palabra_secreta)
