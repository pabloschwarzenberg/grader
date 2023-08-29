import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["manzana", "perro", "gato", "elefante", "avion"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = len(palabra_secreta) // 3  # Mostrar aproximadamente un tercio de las letras

    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes 7 intentos para adivinar la palabra.")

    intentos_restantes = 7
    while intentos_restantes > 0:
        print("\nPalabra:", palabra_oculta)
        print("Intentos restantes:", intentos_restantes)
        opcion = input("Ingresa una letra o arriesga la palabra completa: ")

        if len(opcion) == 1:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)
            if opcion not in palabra_secreta:
                intentos_restantes -= 1
        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones, has adivinado la palabra secreta!")
                break
            else:
                intentos_restantes -= 1

    if intentos_restantes == 0:
        print("¡Agotaste tus intentos! La palabra secreta era:", palabra_secreta)
         