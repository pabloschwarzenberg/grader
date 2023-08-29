import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada[i] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "internet", "tecnologia"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta) - 1))

    intentos = 7
    while intentos > 0:
        print("Palabra actual:", letras_mostradas)
        print("Intentos restantes:", intentos)
        opcion = input("Ingresa una letra o arriésgate con la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if opcion in palabra_secreta:
                print("¡Correcto!")
                if "_" not in letras_mostradas:
                    print("¡Has adivinado la palabra secreta:", palabra_secreta, "!")
                    break
            else:
                print("Incorrecto. La letra no está en la palabra.")
                intentos -= 1
        else:
            if opcion == palabra_secreta:
                print("¡Has adivinado la palabra secreta:", palabra_secreta, "!")
                break
            else:
                print("Incorrecto. Esa no es la palabra secreta.")
                intentos -= 1

    if intentos == 0:
        print("¡Se te acabaron los intentos! La palabra secreta era:", palabra_secreta)
