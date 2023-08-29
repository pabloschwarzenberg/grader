import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "leon"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, int(len(palabra_secreta)/2))
    intentos = 7

    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Intentos restantes:", intentos)

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        opcion = opcion.lower()

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if opcion not in palabra_secreta:
                intentos -= 1
        elif opcion == palabra_secreta:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break
        else:
            intentos -= 1

        if "_" not in letras_mostradas:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break

    if intentos == 0:
        print("¡Oh no! Has agotado todos tus intentos. La palabra secreta era:", palabra_secreta)
