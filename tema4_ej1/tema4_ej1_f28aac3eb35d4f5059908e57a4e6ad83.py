import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada[i] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "algoritmo", "desarrollo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, int(len(palabra_secreta) * 0.5))
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene {} letras.".format(len(palabra_secreta)))
    print("Tienes {} intentos para adivinarla.")

    while intentos > 0:
        print("\nPalabra actual: {}".format(letras_mostradas))
        print("Intentos restantes: {}".format(intentos))

        opcion = input("Ingresa una letra o escribe 'arriesgar' para adivinar la palabra completa: ")

        if opcion == "arriesgar":
            arriesgo = input("Ingresa la palabra completa: ")
            if arriesgo == palabra_secreta:
                print("\n¡Felicidades! Adivinaste la palabra secreta.")
                break
            else:
                print("\n¡Incorrecto! La palabra secreta no es '{}'.".format(arriesgo))
                intentos -= 1
        else:
            letra_ingresada = opcion.lower()
            if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
                print("\nPor favor, ingresa una sola letra.")
                continue

            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, letra_ingresada)
            if letra_ingresada not in palabra_secreta:
                print("\nLa letra '{}' no está en la palabra secreta.".format(letra_ingresada))
                intentos -= 1

    if intentos == 0:
        print("\n¡Perdiste! La palabra secreta era '{}'.".format(palabra_secreta))      