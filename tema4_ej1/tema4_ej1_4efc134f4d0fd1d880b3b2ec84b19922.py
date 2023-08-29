import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for i in letras_ocultas:
        palabra_oculta[i] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_nueva = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_nueva += letra
        else:
            palabra_nueva += palabra_mostrada[i]
    return palabra_nueva

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "algoritmo", "variable"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)

    intentos = 7
    while intentos > 0:
        print(f"Palabra: {palabra_mostrada}")
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion in palabra_secreta:
                print("¡Letra correcta!")
            else:
                intentos -= 1
                print(f"Letra incorrecta. Intentos restantes: {intentos}")
        else:
            if opcion == palabra_secreta:
                print("¡Adivinaste la palabra!")
                break
            else:
                intentos -= 1
                print(f"Palabra incorrecta. Intentos restantes: {intentos}")

    if intentos == 0:
        print(f"Se acabaron los intentos. La palabra secreta era: {palabra_secreta}")
