import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_actualizada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_actualizada += letra
        else:
            palabra_actualizada += palabra_mostrada[i]
    return palabra_actualizada

if __name__ == "__main__":
    palabras_secretas = ["elefante", "guitarra", "playa", "manzana", "campana"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta.")
    print("Tienes 7 intentos para adivinar la palabra.")

    while intentos > 0:
        print("\nPalabra actual:", letras_mostradas)
        print("Intentos restantes:", intentos)
        
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        else:
            if opcion == palabra_secreta:
                print("\n¡Felicidades! Adivinaste la palabra secreta.")
                break
            else:
                print("\n¡Incorrecto! La palabra secreta no es", opcion)
        
        intentos -= 1

    if intentos == 0:
        print("\n¡Lo siento! Has agotado tus intentos.")
        print("La palabra secreta era:", palabra_secreta)
