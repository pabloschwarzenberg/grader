import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    palabra_oculta = "".join(letras_ocultas)
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_secreta = list(palabra_secreta)
    letras_mostrada = list(palabra_mostrada)
    for i in range(len(letras_secreta)):
        if letras_secreta[i] == letra:
            letras_mostrada[i] = letra
    palabra_nueva = "".join(letras_mostrada)
    return palabra_nueva

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "insecto", "alas", "oruga"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    intentos = 7

    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Intentos restantes:", intentos)
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if opcion not in palabra_secreta:
                intentos -= 1
        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! Has adivinado la palabra secreta.")
                break
            else:
                print("Palabra incorrecta. Sigue intentando.")
                intentos -= 1

    if intentos == 0:
        print("Se acabaron los intentos. La palabra secreta era:", palabra_secreta)

