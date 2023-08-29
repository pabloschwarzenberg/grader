import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "mono"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)-1))

    intentos = 7
    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Intentos restantes:", intentos)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        elif opcion == palabra_secreta:
            print("¡Felicidades! ¡Adivinaste la palabra!")
            break
        else:
            print("Palabra incorrecta. Has perdido un intento.")
            intentos -= 1

        if letras_mostradas == palabra_secreta:
            print("¡Felicidades! ¡Adivinaste la palabra!")
            break

    if intentos == 0:
        print("¡Has agotado tus intentos! La palabra secreta era:", palabra_secreta)