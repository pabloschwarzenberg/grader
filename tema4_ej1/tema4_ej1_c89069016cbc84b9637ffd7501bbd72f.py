import random

def escoger_palabra_secreta():
    palabras = ["python", "programacion", "computadora", "desarrollo", "algoritmo"]
    palabra_secreta = random.choice(palabras)
    return palabra_secreta

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_oculta, letra):
    nueva_palabra_oculta = list(palabra_oculta)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra_oculta[indice] = letra
    return "".join(nueva_palabra_oculta)

if __name__ == "__main__":
    palabra_secreta = escoger_palabra_secreta()
    letras_ocultas = random.randint(1, len(palabra_secreta))
    palabra_oculta = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta.")
    print("La palabra tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    while intentos > 0:
        print("\nPalabra:", palabra_oculta)
        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(letra) == 1:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, letra)
            if letra not in palabra_secreta:
                intentos -= 1
                print("La letra", letra, "no está en la palabra. Te quedan", intentos, "intentos.")
        elif len(letra) == len(palabra_secreta) and letra.lower() == palabra_secreta.lower():
            print("¡Felicidades! Adivinaste la palabra secreta.")
            break
        else:
            print("La palabra ingresada no es válida.")

    if intentos == 0:
        print("\n¡Perdiste! La palabra secreta era:", palabra_secreta)
