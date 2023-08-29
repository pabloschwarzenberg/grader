import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    nueva_palabra = list(palabra)
    for indice in letras_ocultas:
        nueva_palabra[indice] = "_"
    return "".join(nueva_palabra)

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = list(palabra)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra[indice] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_oculta = ocultar_letras(palabra_secreta, letras_ocultas)

    print("¡Bienvenido al juego de adivinar palabras con letras ocultas!")
    print("La palabra secreta tiene {len(palabra_secreta)} letras y {letras_ocultas} están ocultas.")

    while True:
        print("\nPalabra: ", palabra_oculta)
        opcion = input("Ingresa una letra o arriesga la palabra completa: ")

        if len(opcion) == 1:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! Has adivinado la palabra.")
                break
            else:
                print("Palabra incorrecta. Sigue intentando.")

        if palabra_oculta == palabra_secreta:
            print("¡Felicitaciones! Has adivinado la palabra.")
            break
