import random

def ocultar_letras(palabra, cantidad):
    ocultada = list(palabra)
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    for indice in letras_ocultas:
        ocultada[indice] = "_"
    return "".join(ocultada)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra[i] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tortuga"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)

    intentos = 7
    while intentos > 0:
        print("Palabra actual:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        opcion = input("Ingrese una letra o adivine la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! Has adivinado la palabra.")
                break
            else:
                print("La palabra ingresada es incorrecta.")

        if palabra_mostrada == palabra_secreta:
            print("¡Felicitaciones! Has adivinado la palabra.")
            break

        intentos -= 1

    if intentos == 0:
        print("¡Oh no! Has agotado tus intentos. La palabra secreta era:", palabra_secreta)
