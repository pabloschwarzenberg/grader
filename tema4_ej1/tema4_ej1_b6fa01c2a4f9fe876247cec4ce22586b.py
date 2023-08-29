import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = '_'
    return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_actualizada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_actualizada[i] = letra
    return ''.join(palabra_actualizada)

if __name__ == "__main__":
    palabras_secretas = ["elefante", "guitarra", "programacion", "manzana", "universidad"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta)-1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)

    intentos = 7
    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra.")
                break
        elif opcion == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra completa.")
            break

        intentos -= 1

    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)

         