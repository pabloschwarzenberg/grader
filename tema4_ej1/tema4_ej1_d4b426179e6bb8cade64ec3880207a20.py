import random

def ocultar_letras(palabra, cantidad):
    ocultada = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        ocultada[indice] = "_"
    return "".join(ocultada)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "desarrollo", "juego"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = len(palabra_secreta) // 2
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("Tienes 7 intentos para adivinar la palabra.")

    while intentos > 0:
        print("Palabra actual:", palabra_mostrada)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) > 1:
            if opcion == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra secreta:", palabra_secreta)
            else:
                print("¡Oh no! La palabra ingresada no es correcta. La palabra secreta era:", palabra_secreta)
            break

        if opcion in palabra_secreta:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra secreta:", palabra_secreta)
                break
        else:
            intentos -= 1
            print("Letra incorrecta. Te quedan", intentos, "intentos.")

    if intentos == 0:
        print("¡Oh no! Te quedaste sin intentos. La palabra secreta era:", palabra_secreta)
         