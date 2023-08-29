import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "caballo", "elefante", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinar la palabra.")

    while intentos > 0:
        print("Palabra oculta:", palabra_oculta)
        entrada = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if entrada == palabra_secreta:
            print("¡Felicitaciones! Adivinaste la palabra secreta:", palabra_secreta)
            break
        elif len(entrada) == 1:
            letra_ingresada = entrada.lower()
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, letra_ingresada)
            if palabra_oculta == palabra_secreta:
                print("¡Felicitaciones! Adivinaste la palabra secreta:", palabra_secreta)
                break
            else:
                intentos -= 1
                print("Incorrecto. Te quedan", intentos, "intentos.")
        else:
            print("¡Ups! Eso no es una letra válida. Intenta nuevamente.")

    if intentos == 0:
        print("¡Lo siento! Te quedaste sin intentos. La palabra secreta era:", palabra_secreta)

         