import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_actualizada = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            palabra_actualizada[indice] = caracter
    return "".join(palabra_actualizada)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "desarrollo", "juego", "computadora"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Adivina la palabra.")
    print("Palabra:", palabra_mostrada)
    print("Tienes",intentos, "intentos")

    while intentos > 0:
        if "_" not in palabra_mostrada:
            print("¡Felicidades! Has adivinado la palabra.")
            break

        entrada = input("Ingresa una letra o arriésgate con la palabra completa: ")

        if len(entrada) == 1:
            nueva_palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, entrada)
            if nueva_palabra_mostrada == palabra_mostrada:
                intentos -= 1
                print("Letra incorrecta. Intenta de nuevo.")
            else:
                palabra_mostrada = nueva_palabra_mostrada
                print("Palabra:", palabra_mostrada)
        elif len(entrada) > 1:
            if entrada == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra.")
            else:
                intentos -= 1
                print("Palabra incorrecta. Intenta de nuevo.")
        
        print ("Tienes", intentos, "intentos")

    if "_" in palabra_mostrada:
        print("te has quedado sin intentos. La palabra secreta era:", palabra_secreta)