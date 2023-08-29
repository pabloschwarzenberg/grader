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
    palabras_secretas = ["python", "programacion", "computadora", "juego", "adivinar"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, len(palabra_secreta) // 2)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras. Adivina cuál es.")

    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Intentos restantes:", intentos)
        opcion = input("Ingresa una letra o escribe 'arriesgar' para adivinar la palabra completa: ")

        if opcion == "arriesgar":
            intento = input("Adivina la palabra: ")
            if intento == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra secreta:", palabra_secreta)
                break
            else:
                print("Incorrecto. Sigue intentando.")
        elif len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if "_" not in letras_mostradas:
                print("¡Felicidades! Adivinaste la palabra secreta:", palabra_secreta)
                break
            else:
                print("Letra correcta. Sigue intentando.")
        else:
            print("Opción no válida. Intenta nuevamente.")

        intentos -= 1

    if intentos == 0:
        print("Se acabaron los intentos. La palabra secreta era:", palabra_secreta)