import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = '_'
    return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ''
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "oruga", "pupa", "insecto"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta.")
    print(f"La palabra secreta tiene {len(palabra_secreta)} letras. Adivina qué palabra es.")

    while intentos > 0:
        print(f"Palabra actual: {palabra_mostrada}")
        print(f"Tienes {intentos} intentos restantes.")

        entrada = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(entrada) == 1:  # El jugador ingresó una letra
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, entrada)
            if entrada in palabra_secreta:
                print("¡Bien! Has encontrado una letra.")
                if palabra_mostrada == palabra_secreta:
                    print(f"¡Felicidades! Has adivinado la palabra secreta: {palabra_secreta}")
                    break
            else:
                print("Oops, esa letra no está en la palabra secreta.")
                intentos -= 1
        else:  # El jugador arriesgó a decir la palabra completa
            if entrada == palabra_secreta:
                print(f"¡Felicidades! Has adivinado la palabra secreta: {palabra_secreta}")
            else:
                print(f"¡Oops! La palabra ingresada no es correcta. La palabra secreta era: {palabra_secreta}")
            break

    if intentos == 0:
        print(f"¡Se acabaron los intentos! La palabra secreta era: {palabra_secreta}")
