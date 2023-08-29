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
    palabras_secretas = ["gato", "perro", "elefante", "tigre", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, int(len(palabra_secreta)/2))
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta.")
    print("La palabra tiene", len(palabra_secreta), "letras. Tienes 7 intentos.")

    while intentos > 0:
        print("Palabra actual:", letras_mostradas)
        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(letra) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, letra)
            if letra in palabra_secreta:
                print("¡La letra está en la palabra secreta!")
            else:
                print("La letra no está en la palabra secreta.")
                intentos -= 1
        elif letra == palabra_secreta:
            print("¡Felicitaciones! ¡Has adivinado la palabra secreta!")
            break
        else:
            print("Lo siento, has perdido. La palabra secreta era:", palabra_secreta)
            break

        if letras_mostradas == palabra_secreta:
            print("¡Felicitaciones! ¡Has adivinado la palabra secreta!")
            break

        print("Intentos restantes:", intentos)

        if intentos == 0:
            print("Lo siento, has perdido. La palabra secreta era:", palabra_secreta)
            break