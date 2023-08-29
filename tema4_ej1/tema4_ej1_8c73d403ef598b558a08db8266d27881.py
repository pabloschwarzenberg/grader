import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra[i] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "rinoceronte"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))

    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene {} letras.".format(len(palabra_secreta)))
    print("Tienes 7 intentos para adivinarla.")

    while intentos > 0:
        print("Palabra actual: {}".format(palabra_mostrada))
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        opcion = opcion.lower()

        if len(opcion) == 1:
            if opcion in palabra_secreta:
                palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
                print("¡Correcto! La letra '{}' está en la palabra.".format(opcion))
            else:
                print("La letra '{}' no está en la palabra.".format(opcion))
                intentos -= 1
        else:
            if opcion == palabra_secreta:
                palabra_mostrada = opcion
                print("bien hecho.")
                break
            else:
                print("la palabra es incorrecta.")
                intentos -= 1

        print("Intentos restantes: {}".format(intentos))
        print()

    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra secreta era '{}'.".format(palabra_secreta))
