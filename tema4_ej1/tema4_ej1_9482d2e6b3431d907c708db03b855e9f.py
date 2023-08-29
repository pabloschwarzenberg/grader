import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    letras_a_ocultar = random.sample(range(len(palabra)), cantidad)
    for indice in letras_a_ocultar:
        letras_ocultas[indice] = "_"
    palabra_oculta = "".join(letras_ocultas)
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_mostradas = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            letras_mostradas[indice] = letra
    palabra_nueva = "".join(letras_mostradas)
    return palabra_nueva

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta) - 1))
    intentos = 7

    print("Adivina la palabra secreta:")
    print(letras_mostradas)

    while intentos > 0:
        letra = input("Ingresa una letra o intenta adivinar la palabra completa: ")

        if len(letra) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, letra)
            print(letras_mostradas)

            if letras_mostradas == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra secreta.")
                break

        elif len(letra) > 1:
            if letra == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra secreta.")
                break
            else:
                print("¡Incorrecto! La palabra ingresada no es la correcta.")
                intentos -= 1
                print("Intentos restantes:", intentos)

        else:
            print("Por favor, ingresa una letra o una palabra válida.")

        if intentos == 0:
            print("¡Perdiste! No lograste adivinar la palabra secreta.")
            print("La palabra secreta era:", palabra_secreta)
