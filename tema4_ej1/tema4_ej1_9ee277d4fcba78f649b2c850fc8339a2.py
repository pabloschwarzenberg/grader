import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_oculta, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_oculta[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "leopardo", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Bienvenido al juego de adivinar palabras!")
    print("Adivina la palabra secreta. Tienes 7 intentos.")

    while intentos > 0:
        print("Palabra actual:", palabra_oculta)
        opcion = input("Ingresa una letra o arriésgate con la palabra completa: ")

        if len(opcion) == 1:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)
        elif opcion == palabra_secreta:
            print("Felicitaciones, ¡adivinaste la palabra secreta!")
            break
        else:
            print("La palabra ingresada es incorrecta.")

        intentos -= 1
        print("Intentos restantes:", intentos)

    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)


         