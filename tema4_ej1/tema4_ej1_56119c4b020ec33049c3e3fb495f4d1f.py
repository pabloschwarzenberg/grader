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
    palabras_secretas = ["python", "programacion", "computadora", "juego", "adivinar"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = len(palabra_secreta) // 2  # Mostrar la mitad de las letras de la palabra secreta inicialmente
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinarla.")
    print("Palabra inicial:", palabra_mostrada)

    while intentos > 0:
        if "_" not in palabra_mostrada:
            print("¡Felicidades! ¡Has adivinado la palabra secreta!")
            break

        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(letra) == 1:
            nueva_palabra = revisar_letra(palabra_secreta, palabra_mostrada, letra)
            if nueva_palabra == palabra_mostrada:
                intentos -= 1
                print("Letra incorrecta. Te quedan", intentos, "intentos.")
            else:
                palabra_mostrada = nueva_palabra
                print("¡Letra encontrada!")
        else:
            if letra == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra secreta!")
                break
            else:
                intentos -= 1
                print("Palabra incorrecta. Te quedan", intentos, "intentos.")

    if intentos == 0:
        print("¡Oh no! Te has quedado sin intentos. La palabra secreta era:", palabra_secreta)

         