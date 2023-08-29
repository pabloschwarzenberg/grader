import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    posiciones_ocultas = random.sample(range(len(palabra)), cantidad)
    for pos in posiciones_ocultas:
        letras_ocultas[pos] = "_"
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_oculta, letra):
    nueva_palabra_oculta = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_oculta += letra
        else:
            nueva_palabra_oculta += palabra_oculta[i]
    return nueva_palabra_oculta

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, int(len(palabra_secreta) / 2))
    intentos = 7
    
    print("Bienvenido al juego de adivinar la palabra secreta.")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes 7 intentos para adivinarla.")

    while intentos > 0:
        print("\nPalabra:", letras_ocultas)
        print("Intentos restantes:", intentos)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_ocultas = revisar_letra(palabra_secreta, letras_ocultas, opcion)
            if opcion not in palabra_secreta:
                intentos -= 1
        elif opcion == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break
        else:
            intentos -= 1

    if intentos == 0:
        print("\n¡Has agotado tus intentos! La palabra secreta era:", palabra_secreta)

    print("\nGracias por jugar. ¡Hasta la próxima!")
