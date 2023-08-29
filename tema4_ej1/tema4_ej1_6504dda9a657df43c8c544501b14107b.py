import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_mostrada = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            palabra_mostrada[indice] = letra
    return "".join(palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "algoritmo", "desarrollo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, len(palabra_secreta) // 2)

    intentos = 7
    while intentos > 0:
        print("Palabra:", letras_mostradas)
        opcion = input("Ingrese una letra o la palabra completa: ")

        if opcion == palabra_secreta:
            print("¡Felicitaciones! Adivinaste la palabra secreta:", palabra_secreta)
            break
        elif len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        else:
            print("Palabra incorrecta. Intenta de nuevo.")
        
        intentos -= 1

    if intentos == 0:
        print("¡Agotaste tus intentos! La palabra secreta era:", palabra_secreta)
