import random

def ocultar_letras(palabra, cantidad):
    """Oculta la cantidad de letras especificada en la palabra secreta."""
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = '_'
    return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    """Revisa si la letra ingresada por el jugador está en la palabra secreta y actualiza la palabra mostrada."""
    palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_mostrada[i] = letra
    return ''.join(palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ['lepidoptero', 'murcielago', 'ornitorrinco', 'hipopotamo']
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    
    print("Bienvenido al juego de adivinanzas de palabras!")
    print("La palabra secreta tiene {} letras ocultas.".format(letras_mostradas))
    print("Palabra mostrada:", palabra_mostrada)
    print()
    
    intentos = 7
    while intentos > 0:
        entrada = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(entrada) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, entrada)
            print("Palabra mostrada:", palabra_mostrada)
            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
                break
        elif entrada == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break
        else:
            print("Incorrecto.")
            intentos -= 1
            print("Intentos restantes:", intentos)
        print()
    
    if intentos == 0:
        print("¡Lo siento! Has agotado tus intentos. La palabra secreta era:", palabra_secreta)
