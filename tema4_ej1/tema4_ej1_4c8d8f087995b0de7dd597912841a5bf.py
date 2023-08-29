import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra_mostrada[indice] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["manzana", "pera", "platano", "sandia", "fresa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)-1))
    intentos = 7

    print("Adivina la palabra secreta. Tienes 7 intentos.")

    while intentos > 0:
        print("Palabra:", letras_mostradas)
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
                break
            else:
                print("Palabra incorrecta. Sigue intentando.")

        intentos -= 1
        print("Intentos restantes:", intentos)

    if intentos == 0:
        print("Has agotado todos tus intentos. La palabra secreta era:", palabra_secreta)
