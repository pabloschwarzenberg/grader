import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
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

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "tortuga"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("Tienes 7 intentos para adivinar la palabra.")

    while intentos > 0:
        print("Palabra actual:", palabra_mostrada)
        print("Intentos restantes:", intentos)
        opcion = input("Ingresa una letra o arriesga la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion in palabra_mostrada:
                print("¡Correcto! La letra está en la palabra.")
            else:
                print("La letra no está en la palabra. ¡Inténtalo de nuevo!")
                intentos -= 1
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra.")
                break
            else:
                print("Palabra incorrecta. ¡Inténtalo de nuevo!")
                intentos -= 1

    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)
