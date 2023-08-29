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
    palabras_secretas = ["python", "programacion", "ordenador", "juego"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene {} letras. Tienes {} intentos.".format(len(palabra_secreta), intentos))
    print("Palabra mostrada: {}".format(palabra_mostrada))

    while intentos > 0:
        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(letra) > 1:
            if letra == palabra_secreta:
                print("¡Felicitaciones! ¡Has adivinado la palabra secreta!")
            else:
                print("Lo siento, esa no es la palabra secreta. ¡Has perdido!")
            break

        if letra in palabra_secreta:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
            print("¡Muy bien! La letra está en la palabra secreta.")
            print("Palabra mostrada: {}".format(palabra_mostrada))
            if palabra_mostrada == palabra_secreta:
                print("¡Felicitaciones! ¡Has adivinado la palabra secreta!")
                break
        else:
            print("La letra no está en la palabra secreta.")
            intentos -= 1
            print("Te quedan {} intentos.".format(intentos))

        if intentos == 0:
            print("Lo siento, has agotado todos tus intentos. ¡Has perdido!")
            print("La palabra secreta era: {}".format(palabra_secreta))
         