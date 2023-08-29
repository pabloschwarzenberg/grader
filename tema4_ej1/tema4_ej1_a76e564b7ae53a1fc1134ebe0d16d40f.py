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

# Lista de palabras secretas
palabras_secretas = ["perro", "gato", "sol", "programacion", "computador"]

palabra_secreta = random.choice(palabras_secretas)

letras_mostradas = random.randint(1, len(palabra_secreta) - 1)

palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)

# Número de intentos
intentos_restantes = 7

# Juego principal
if __name__ == "__main__":
    print("¡Bienvenido al juego!")
    print("Tienes 7 intentos para adivinar la palabra secreta.")
    print("La palabra tiene", len(palabra_secreta), "letras.")
    print("La palabra oculta es:", palabra_oculta)

    while intentos_restantes > 0:
        print("Intentos restantes:", intentos_restantes)

        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) > 1:
            if opcion == palabra_secreta:
                print("Adivinaste la palabra secreta:", palabra_secreta)
                break
            else:
                print("No es la palabra correcta. intenta de nuevo.")
                intentos_restantes -= 1
        else:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)
            print("La palabra oculta es:", palabra_oculta)

            if palabra_oculta == palabra_secreta:
                print("Adivinaste la palabra secreta:", palabra_secreta)
                break

            intentos_restantes -= 1

    if intentos_restantes == 0:
        print("Se acabaron los intentos. La palabra secreta era:", palabra_secreta)
