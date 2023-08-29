import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada[i] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["elefante", "guitarra", "computadora", "manzana", "futbol"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    while intentos > 0:
        print(f"Palabra actual: {palabra_mostrada}")
        print(f"Intentos restantes: {intentos}")
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        
        if len(opcion) == 1:  # El jugador ingresó una letra
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion not in palabra_mostrada:
                intentos -= 1
        elif opcion == palabra_secreta:  # El jugador arriesgó la palabra completa
            print("¡Felicitaciones! ¡Has adivinado la palabra!")
            break
        else:
            print("Palabra incorrecta. Sigue intentando.")

        if "_" not in palabra_mostrada:
            print("¡Felicitaciones! ¡Has adivinado la palabra!")
            break

    if intentos == 0:
        print("Lo siento, has agotado tus intentos. ¡La palabra secreta era:", palabra_secreta, "!")    