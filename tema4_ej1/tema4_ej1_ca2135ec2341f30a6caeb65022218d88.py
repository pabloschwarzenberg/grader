import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    letras_ocultas_indices = random.sample(range(len(palabra)), cantidad)
    for indice in letras_ocultas_indices:
        letras_ocultas[indice] = "_"
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "leon", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, int(len(palabra_secreta) * 0.5))
    intentos_restantes = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras y se han ocultado algunas.")

    while intentos_restantes > 0:
        print("Palabra:", letras_ocultas)
        print("Intentos restantes:", intentos_restantes)

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_ocultas = revisar_letra(palabra_secreta, letras_ocultas, opcion)
            if opcion in palabra_secreta:
                print("¡Buena elección! La letra", opcion, "aparece en la palabra.")
            else:
                print("Lo siento, la letra", opcion, "no aparece en la palabra.")
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
                break
            else:
                print("Lo siento, esa no es la palabra correcta.")

        intentos_restantes -= 1

    if intentos_restantes == 0:
        print("Has agotado tus intentos. La palabra secreta era:", palabra_secreta)
         