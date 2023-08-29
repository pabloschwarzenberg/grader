import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra_mostrada[indice] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "juego"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))

    intentos = 7
    while intentos > 0:
        print("Palabra: ", letras_mostradas)
        print("Intentos restantes:", intentos)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) > 1:  # Se arriesgó a decir la palabra completa
            if opcion.lower() == palabra_secreta:
                print("¡Adivinaste la palabra!")
                break
            else:
                print("No es la palabra correcta. Sigue intentando.")
                intentos -= 1
        else:  # Se ingresó una letra
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion.lower())
            if letras_mostradas == palabra_secreta:
                print("¡Adivinaste la palabra!")
                break
            elif opcion.lower() not in palabra_secreta:
                print("La letra no está en la palabra. Sigue intentando.")
                intentos -= 1
            else:
                print("¡La letra está en la palabra!")

    if intentos == 0:
        print("¡Te quedaste sin intentos! La palabra secreta era:", palabra_secreta)
