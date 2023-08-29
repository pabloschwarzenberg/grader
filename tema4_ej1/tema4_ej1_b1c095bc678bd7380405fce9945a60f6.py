import random

def ocultar_letras(palabra, cantidad):
    ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada[i] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "adivinar", "jugador"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))

    intentos = 7
    while intentos > 0:
        print("Palabra:", letras_mostradas)
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) > 1:
            if opcion == palabra_secreta:
                print("¡Felicidades, has adivinado la palabra secreta!")
                break
            else:
                print("¡Incorrecto! La palabra secreta no es", opcion)
                intentos -= 1
        else:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if opcion in palabra_secreta:
                print("¡Correcto!")
                if "_" not in letras_mostradas:
                    print("¡Felicidades, has adivinado la palabra secreta!")
                    break
            else:
                print("¡Incorrecto!")
                intentos -= 1

        print("Intentos restantes:", intentos)

    if intentos == 0:
        print("¡Lo siento, has agotado tus intentos!")
        print("La palabra secreta era:", palabra_secreta)

         