import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        letras_ocultas[indice] = '_'
    return ''.join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_secreta = list(palabra_secreta)
    palabra_mostrada = list(palabra_mostrada)
    for i in range(len(letras_secreta)):
        if letras_secreta[i] == letra:
            palabra_mostrada[i] = letra
    return ''.join(palabra_mostrada)

# Lista de palabras secretas
palabras_secretas = ['lepidoptero', 'murcielago', 'serpiente', 'elefante', 'tortuga']

# Escoger una palabra al azar
palabra_secreta = random.choice(palabras_secretas)

# Determinar cuántas letras ocultar
cantidad_letras_ocultas = random.randint(1, len(palabra_secreta))

# Ocultar letras en la palabra secreta
palabra_mostrada = ocultar_letras(palabra_secreta, cantidad_letras_ocultas)

# Juego
print("Adivina la palabra secreta:")
print(palabra_mostrada)

while True:
    opcion = input("R ")

    if len(opcion) == 1:
        palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        print(palabra_mostrada)

        if palabra_mostrada == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break
    else:
        if opcion == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break
        else:
            print("La palabra ingresada no es correcta.")
