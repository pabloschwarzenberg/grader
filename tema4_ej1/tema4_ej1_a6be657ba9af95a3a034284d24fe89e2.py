import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    nueva_palabra = list(palabra)
    for i in letras_ocultas:
        nueva_palabra[i] = "_"
    return "".join(nueva_palabra)

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = list(palabra)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra[i] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "python", "programacion", "computadora", "internet"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_oculta = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    print("¡Adivina la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras, pero algunas están ocultas.")
    print("Tienes", intentos, "intentos.")

    while intentos > 0:
        print("Palabra actual:", palabra_oculta)
        opcion = input("Ingresa una letra o arriésgate con la palabra completa: ")

        if len(opcion) == 1:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)

            if opcion in palabra_secreta:
                print("¡Correcto! La letra está en la palabra.")
            else:
                print("Incorrecto. La letra no está en la palabra.")
                intentos -= 1
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra.")
                break
            else:
                print("Incorrecto. Esa no es la palabra secreta.")
                intentos -= 1

    if intentos == 0:
        print("¡Perdiste! Te quedaste sin intentos.")
        print("La palabra secreta era:", palabra_secreta)
