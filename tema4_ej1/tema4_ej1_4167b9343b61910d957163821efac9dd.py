import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = '_'
    return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ''
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "juego", "aventura"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    intentos = 7

    print("Bienvenido a Adivina la Palabra!")
    print("La palabra a adivinar tiene", len(palabra_secreta), "letras.")

    while intentos > 0:
        print("Palabra actual:", letras_mostradas)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if opcion == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra.")
            break

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        else:
            print("¡Intento fallido! La palabra completa no es correcta.")

        intentos -= 1

        if letras_mostradas == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra.")
            break

    if intentos == 0:
        print("¡No lograste adivinar la palabra! La palabra era:", palabra_secreta)
