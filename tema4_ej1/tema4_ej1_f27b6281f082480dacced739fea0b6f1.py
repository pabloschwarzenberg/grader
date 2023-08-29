         import random
def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_actualizada = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            palabra_actualizada[indice] = letra
    return "".join(palabra_actualizada)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "desarrollo", "aprendizaje"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = len(palabra_secreta) // 2

    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras y tienes", intentos, "intentos.")

    while intentos > 0:
        print("\nPalabra:", palabra_mostrada)

        opcion = input("¿Quieres ingresar una letra (L) o arriesgar la palabra completa (P)? ").lower()

        if opcion == "l":
            letra = input("Ingresa una letra: ")
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
            if letra not in palabra_secreta:
                intentos -= 1
                print("La letra no está en la palabra. Te quedan", intentos, "intentos.")
        elif opcion == "p":
            palabra_arriesgada = input("Ingresa la palabra completa: ")
            if palabra_arriesgada == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra.")
            else:
                intentos = 0
                print("¡Incorrecto! La palabra secreta era:", palabra_secreta)
        else:
            print("Opción inválida. Intenta nuevamente.")

    if intentos == 0:
        print("\n¡Te quedaste sin intentos! La palabra secreta era:", palabra_secreta)
