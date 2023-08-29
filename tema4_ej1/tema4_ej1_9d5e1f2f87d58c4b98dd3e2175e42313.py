import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra[indice] = caracter
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["elefante", "guitarra", "computadora", "programacion", "felicidad"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("¡Bienvenido a Adivina la Palabra!")
    print("Tienes 7 intentos para adivinar la palabra secreta.")
    print("La palabra tiene", len(palabra_secreta), "letras.")

    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)
        opcion = input("Ingresa una letra o arriesga la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion in palabra_secreta:
                print("¡Correcto! La letra", opcion, "está en la palabra.")
            else:
                print("La letra", opcion, "no está en la palabra.")
        else:
            if opcion == palabra_secreta:
                print("¡Adivinaste la palabra!")
                break
            else:
                print("¡Incorrecto! Esa no es la palabra.")

        intentos -= 1
        print("-------------------")

    if intentos == 0:
        print("Se acabaron los intentos. La palabra secreta era:", palabra_secreta)
