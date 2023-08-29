import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)

    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"

    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_actualizada = list(palabra_mostrada)

    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_actualizada[i] = letra

    return "".join(palabra_actualizada)

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)

    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)

    intentos = 7

    while intentos > 0:
        print("Palabra: {palabra_mostrada}")
        print("Intentos restantes: {intentos}")

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Ha adivinado la palabra secreta.")
                break
            else:
                print("Palabra incorrecta.")

        intentos -= 1

    if intentos == 0:
        print("Se han acabado los intentos. ¡Perdiste!")

        print("La palabra secreta era: {palabra_secreta}")