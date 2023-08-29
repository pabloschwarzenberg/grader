import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_ocultas = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            letras_ocultas[i] = letra
    return "".join(letras_ocultas)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "insecto", "oruga", "alas"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)-1))

    intentos = 7
    while intentos > 0:
        print("Palabra actual:", letras_ocultas)
        print("Intentos restantes:", intentos)

        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_ocultas = revisar_letra(palabra_secreta, letras_ocultas, opcion)
        elif opcion == palabra_secreta:
            letras_ocultas = palabra_secreta
        else:
            print("¡Palabra incorrecta!")
            intentos -= 1

        if letras_ocultas == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra secreta:", palabra_secreta)
            break

    if intentos == 0:
        print("¡Se acabaron los intentos! La palabra secreta era:", palabra_secreta)
