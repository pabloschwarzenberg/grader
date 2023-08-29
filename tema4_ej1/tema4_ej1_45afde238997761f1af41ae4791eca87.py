import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_mostrada = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            palabra_mostrada[indice] = letra
    return "".join(palabra_mostrada)

def jugar_adivina_palabra():
    palabras_secretas = ["gato", "perro", "elefante", "leopardo", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos_restantes = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("Tienes 7 intentos para adivinar la palabra.")

    while intentos_restantes > 0:
        print("Palabra actual:", palabra_mostrada)
        print("Intentos restantes:", intentos_restantes)

        opcion = input("¿Deseas ingresar una letra o arriesgar la palabra completa? (L/P): ")

        if opcion.upper() == "L":
            letra = input("Ingresa una letra: ")
            if letra in palabra_secreta:
                palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
                if palabra_mostrada == palabra_secreta:
                    print("¡Adivinaste la palabra secreta!")
                    print("La palabra era:", palabra_secreta)
                    break
                else:
                    print("¡Letra correcta!")
            else:
                print("Letra incorrecta. Sigue intentando.")
        elif opcion.upper() == "P":
            palabra = input("Ingresa la palabra completa: ")
            if palabra == palabra_secreta:
                print("¡Adivinaste la palabra secreta!")
                print("La palabra era:", palabra_secreta)
                break
            else:
                print("Palabra incorrecta. Sigue intentando.")

        intentos_restantes -= 1

    if intentos_restantes == 0:
        print("¡Se te acabaron los intentos!")
        print("La palabra secreta era:", palabra_secreta)

if __name__ == "__main__":
    jugar_adivina_palabra()

         