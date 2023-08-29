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
    palabras_secretas = ["gato", "perro", "pajaro", "elefante", "tigre", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta) - 1))
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinarla.")

    while intentos > 0:
        print("\nPalabra:", letras_mostradas)
        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(letra) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, letra)
        elif len(letra) > 1:
            if letra == palabra_secreta:
                letras_mostradas = palabra_secreta
                break
            else:
                print("¡Incorrecto! Has perdido un intento.")
                intentos -= 1
        else:
            print("¡Debes ingresar una letra o una palabra!")

        if letras_mostradas == palabra_secreta:
            print("\n¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
            break

        print("Intentos restantes:", intentos)

    if intentos == 0:
        print("\n¡Lo siento! Has agotado todos tus intentos. La palabra secreta era:", palabra_secreta)
