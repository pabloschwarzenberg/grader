import random

def ocultar_letras(palabra, cantidad):
    if cantidad >= len(palabra):
        return "_" * len(palabra)
    else:
        indices_ocultos = random.sample(range(len(palabra)), cantidad)
        palabra_oculta = list(palabra)
        for indice in indices_ocultos:
            palabra_oculta[indice] = "_"
        return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
    palabra_actualizada = list(palabra)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_actualizada[i] = letra
    return "".join(palabra_actualizada)

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "tortuga"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Adivina la palabra secreta: " + palabra_oculta)

    while intentos > 0:
        if "_" not in palabra_oculta:
            print("¡Felicidades! ¡Has adivinado la palabra secreta!")
            break

        if intentos == 1:
            opcion = input("¿Cuál es tu última palabra? ")
            if opcion.lower() == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra secreta!")
            else:
                print("Lo siento, la palabra secreta era '" + palabra_secreta + "'. ¡Mejor suerte la próxima vez!")
            break

        letra = input("Ingresa una letra: ")
        palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, letra)
        print("Palabra actualizada: " + palabra_oculta)

        intentos -= 1

    if intentos == 0:
        print("¡Se acabaron los intentos! La palabra secreta era '" + palabra_secreta + "'. ¡Inténtalo de nuevo!")
