import random

def ocultar_letras(palabra, cantidad):
    posiciones_ocultas = random.sample(range(len(palabra)), cantidad)

    nueva_palabra = ""
    for i in range(len(palabra)):
        if i in posiciones_ocultas:
            nueva_palabra += "_"
        else:
            nueva_palabra += palabra[i]

    return nueva_palabra

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]

    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "aleatorio"]
    palabra_secreta = random.choice(palabras_secretas)
    cantidad_letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, cantidad_letras_ocultas)
    intentos = 7
    adivinado = False

    while intentos > 0 and not adivinado:
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        opcion = input("Ingrese una letra o arriesgue la palabra completa: ")

        if opcion == palabra_secreta:
            adivinado = True
            print("¡Adivinaste la palabra! La palabra secreta era:", palabra_secreta)
        elif len(opcion) == 1:
            nueva_palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if nueva_palabra_mostrada == palabra_mostrada:
                print("La letra no está en la palabra secreta.")
                intentos -= 1
            else:
                palabra_mostrada = nueva_palabra_mostrada
                print("La letra está en la palabra secreta.")
        else:
            print("¡Error! Ingrese solo una letra o arriesgue la palabra completa.")

        print("")

    if intentos == 0 and not adivinado:
        print("Se acabaron los intentos. La palabra secreta era:", palabra_secreta)