import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)

    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"

    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_mostrada = list(palabra_mostrada)

    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_mostrada[i] = letra

    return "".join(palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "insecto", "alas", "oruga"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta) - 1))
    intentos_restantes = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")

    while intentos_restantes > 0:
        print("Palabra actual:", letras_mostradas)
        print("Intentos restantes:", intentos_restantes)

        opcion = input("Ingrese una letra o la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)

            if opcion in palabra_secreta:
                print("¡Bien hecho! La letra está en la palabra secreta.")
            else:
                intentos_restantes -= 1
                print("¡Incorrecto! La letra no está en la palabra secreta.")

        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! Has adivinado la palabra secreta.")
                break
            else:
                intentos_restantes -= 1
                print("¡Incorrecto! La palabra no es la correcta.")

    if intentos_restantes == 0:
        print("¡Oh no! Te has quedado sin intentos. La palabra secreta era:", palabra_secreta)
