import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra_mostrada[indice] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "python", "gato", "programacion", "elefante"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, 2)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene {} letras ocultas: {}".format(letras_mostradas.count("_"), letras_mostradas))

    while intentos > 0:
        if "_" not in letras_mostradas:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break

        print("Tienes {} intentos restantes.".format(intentos))
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) > 1:
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
            else:
                print("Lo siento, esa no es la palabra secreta.")
                intentos -= 1
        else:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            print("Palabra: {}".format(letras_mostradas))

    if intentos == 0:
        print("¡Se acabaron los intentos! La palabra secreta era: {}".format(palabra_secreta))
