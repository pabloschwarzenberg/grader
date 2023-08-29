import random
def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    return "".join(letras_ocultas)
def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_secreta = list(palabra_secreta)
    letras_mostrada = list(palabra_mostrada)
    for i in range(len(letras_secreta)):
        if letras_secreta[i] == letra:
            letras_mostrada[i] = letra
    return "".join(letras_mostrada)
if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "juego", "adivinar"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7
    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)
        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(letra) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
            if "_" not in palabra_mostrada:
                print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
                break
            intentos -= 1
        elif len(letra) > 1:
            if letra == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
                break
            else:
                print("La palabra ingresada no es correcta.")
                intentos -= 1
        else:
            print("Por favor, ingresa una letra o la palabra completa.")
    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)   