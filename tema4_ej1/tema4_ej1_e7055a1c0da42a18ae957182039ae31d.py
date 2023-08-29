import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(letras_ocultas)), cantidad)
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if _name_ == "_main_":
    palabras_secretas = ["elefante", "computadora", "guitarra", "playa", "montaña"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, int(len(palabra_secreta) / 2))
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras. Adivina la palabra mostrada.")
    print("Tienes", intentos, "intentos.")

    while intentos > 0:
        print("Palabra mostrada:", letras_mostradas)
        opcion = input("Ingresa una letra o arriesga la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if opcion in palabra_secreta:
                print("¡Letra correcta!")
            else:
                intentos -= 1
                print("Letra incorrecta. Te quedan", intentos, "intentos.")
        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! Adivinaste la palabra secreta.")
                break
            else:
                intentos -= 1
                print("Palabra incorrecta. Te quedan", intentos, "intentos.")

        if letras_mostradas == palabra_secreta:
            print("¡Felicitaciones! Adivinaste la palabra secreta.")
            break

        if intentos == 0:
            print("Se acabaron tus intentos. La palabra secreta era:", palabra_secreta)