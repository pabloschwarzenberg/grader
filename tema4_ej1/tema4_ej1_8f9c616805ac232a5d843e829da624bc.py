import random

def escoger_palabra_secreta(palabras):
    return random.choice(palabras)

def ocultar_letras(palabra, cantidad):
    ocultas = random.sample(range(len(palabra)), cantidad)
    nueva_palabra = list(palabra)
    for indice in ocultas:
        nueva_palabra[indice] = "_"
    return "".join(nueva_palabra)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = list(palabra_mostrada)
    for i, char in enumerate(palabra_secreta):
        if char == letra:
            nueva_palabra[i] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tigre"]
    palabra_secreta = escoger_palabra_secreta(palabras_secretas)
    letras_mostradas = len(palabra_secreta) // 2
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)

    intentos = 7
    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! Ha adivinado la palabra.")
                break
            else:
                print("La palabra ingresada es incorrecta.")

        if palabra_mostrada == palabra_secreta:
            print("¡Felicitaciones! Ha adivinado la palabra.")
            break

        intentos -= 1

    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)
