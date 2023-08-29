import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_mostrada[i] = letra
    return "".join(palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "insecto", "alas", "naturaleza"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    intentos = 7

    print("¡Bienvenido al juego de adivinar palabras!")
    print("Tienes que adivinar la palabra secreta. Tienes 7 intentos.")
    print(f"La palabra tiene {len(palabra_secreta)} letras. A continuación, te muestro algunas letras:")
    print(letras_mostradas)

    while intentos > 0:
        if "_" not in letras_mostradas:
            print("¡Felicidades! Has adivinado la palabra.")
            break

        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(letra) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, letra)
            print(letras_mostradas)
        else:
            if letra == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra.")
                break
            else:
                print("¡No es la palabra correcta!")

        intentos -= 1

    if "_" in letras_mostradas:
        print(f"¡Agotaste tus intentos! La palabra secreta era: {palabra_secreta}")

