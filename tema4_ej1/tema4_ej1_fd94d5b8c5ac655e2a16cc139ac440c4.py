import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    posiciones_ocultas = random.sample(range(len(palabra)), cantidad)
    for pos in posiciones_ocultas:
        letras_ocultas[pos] = "_"
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_secreta = list(palabra_secreta)
    letras_mostradas = list(palabra_mostrada)
    for i in range(len(letras_secreta)):
        if letras_secreta[i] == letra:
            letras_mostradas[i] = letra
    return "".join(letras_mostradas)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "teclado", "desarrollo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, int(len(palabra_secreta) / 2))

    intentos = 6
    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Intentos restantes:", intentos)

        opcion = input("Ingrese una letra o arriesgue la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if opcion not in palabra_secreta:
                intentos -= 1
        else:
            if opcion == palabra_secreta:
                letras_mostradas = palabra_secreta
                break
            else:
                intentos -= 1

        print()

    if letras_mostradas == palabra_secreta:
        print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
    else:
        print("Has agotado tus intentos. La palabra correcta era:", palabra_secreta)

         