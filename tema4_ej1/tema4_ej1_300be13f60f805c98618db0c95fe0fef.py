import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_oculta, letra):
    nueva_palabra = list(palabra_oculta)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra[i] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "insecto", "oruga", "metamorfosis"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos_restantes = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras y", letras_mostradas, "letras se han ocultado.")
    print("Tienes", intentos_restantes, "intentos para adivinar la palabra.")

    while intentos_restantes > 0:
        print("Palabra oculta:", palabra_oculta)

        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        opcion = opcion.lower()

        if len(opcion) == 1:
            if opcion.isalpha():
                if opcion in palabra_secreta:
                    palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)
                    print("¡Correcto! La letra", opcion, "está en la palabra.")
                else:
                    print("La letra", opcion, "no está en la palabra. Intenta de nuevo.")
                    intentos_restantes -= 1
            else:
                print("Ingresa solo letras. Intenta de nuevo.")
        elif len(opcion) > 1:
            if opcion == palabra_secreta:
                palabra_oculta = opcion
                break
            else:
                print("Esa no es la palabra correcta. Intenta de nuevo.")
                intentos_restantes -= 1
        else:
            print("Ingresa una letra o palabra válida. Intenta de nuevo.")

        print("Intentos restantes:", intentos_restantes)
        print()

    if intentos_restantes > 0:
        print("¡Felicidades! Has adivinado la palabra secreta:", palabra_oculta)
    else:
        print("Has agotado todos tus intentos. La palabra secreta era:", palabra_secreta)
