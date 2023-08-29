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
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "tortuga"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Bienvenido al juego de adivinar palabras!")
    print("Adivina la palabra secreta de longitud" , len(palabra_secreta))
    print("Palabra mostrada: ", palabra_mostrada)

    while intentos > 0:
        if "_" not in palabra_mostrada:
            print("¡Has adivinado la palabra!")
            break

        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(letra) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
            print("Palabra mostrada: " , palabra_mostrada)
        elif letra == palabra_secreta:
            print("Has adivinado la palabra!")
            break
        else:
            print("¡Incorrecto!")
            intentos -= 1
            print("Te quedan", intentos, "intentos")

    if "_" in palabra_mostrada:
        print("Has agotado tus intentos. La palabra secreta era:", palabra_secreta)
