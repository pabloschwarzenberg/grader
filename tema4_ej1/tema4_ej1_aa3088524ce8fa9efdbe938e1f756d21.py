import random
#entrada

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
    palabras_secretas = ["python", "programacion", "computadora", "gato", "casa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras y algunas están ocultas.")
    print("Tienes", intentos, "intentos para adivinarla.")
    print("La palabra mostrada es:", palabra_mostrada)

    while intentos > 0:
        if "_" not in palabra_mostrada:
            print("¡Felicidades! ¡Has adivinado la palabra secreta!")
            break

        print("Ingrese una letra o arriésguese a decir la palabra completa:")
        respuesta = input().lower()

        if len(respuesta) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, respuesta)
            if respuesta not in palabra_secreta:
                intentos -= 1
        elif respuesta == palabra_secreta:
            print("¡Felicidades! ¡Has adivinado la palabra secreta!")
            break
        else:
            intentos -= 1

        print("La palabra mostrada es:", palabra_mostrada)
        print("Intentos restantes:", intentos)

    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)

    
      

         