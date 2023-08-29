import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    ocultas_indices = random.sample(range(len(letras_ocultas)), cantidad)
    for indice in ocultas_indices:
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
    palabras_secretas = ["gato", "perro", "elefante", "leon", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, len(palabra_secreta) // 2)
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    while intentos > 0:
        print("Palabra actual:", letras_ocultas)
        respuesta = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(respuesta) == 1:
            letras_ocultas = revisar_letra(palabra_secreta, letras_ocultas, respuesta)
        elif len(respuesta) > 1:
            if respuesta == palabra_secreta:
                letras_ocultas = palabra_secreta
                break
            else:
                print("¡Palabra incorrecta!")
                intentos -= 1
                print("Tienes", intentos, "intentos restantes.")
        
        if letras_ocultas == palabra_secreta:
            break

    if letras_ocultas == palabra_secreta:
        print("¡Felicitaciones! Has adivinado la palabra secreta:", palabra_secreta)
    else:
        print("¡Agotaste tus intentos! La palabra secreta era:", palabra_secreta)
