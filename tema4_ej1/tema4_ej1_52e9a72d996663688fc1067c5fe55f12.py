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
    palabras_secretas = ["elefante", "guitarra", "computadora", "playa", "montaña"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)

    intentos = 7
    while intentos > 0:
        print("Palabra actual:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if palabra_secreta == palabra_mostrada:
                print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
                break
        elif opcion == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
            break
        else:
            print("Lo siento, esa no es la palabra secreta.")

        intentos -= 1

    if intentos == 0:
        print("¡Has agotado tus intentos! La palabra secreta era:", palabra_secreta)
