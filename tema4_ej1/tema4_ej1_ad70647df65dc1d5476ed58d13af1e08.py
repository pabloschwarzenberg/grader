import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)

    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"

    palabra_oculta = "".join(letras_ocultas)
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""

    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]

    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "leon", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta) - 1))
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta.")
    print("La palabra tiene {} letras.".format(len(palabra_secreta)))
    print("Tienes {} intentos para adivinarla.")

    while intentos > 0:
        print("Palabra: {}".format(letras_mostradas))
        print("Intentos restantes: {}".format(intentos))

        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if opcion not in palabra_secreta:
                intentos -= 1
        else:
            if opcion == palabra_secreta:
                letras_mostradas = opcion
                break
            else:
                intentos -= 1

        if letras_mostradas == palabra_secreta:
            break

    if letras_mostradas == palabra_secreta:
        print("¡Felicitaciones! Adivinaste la palabra secreta: {}".format(palabra_secreta))
    else:
        print("No lograste adivinar la palabra secreta. La palabra era: {}".format(palabra_secreta))
