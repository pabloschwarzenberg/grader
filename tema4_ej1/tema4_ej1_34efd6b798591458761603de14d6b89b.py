def ocultar_letras(palabra,cantidad):
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra_mostrada[indice] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "leopardo", "rinoceronte"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    while intentos > 0:
        print("Palabra actual:", palabra_mostrada)
        print("Intentos restantes:", intentos)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:  # Se ingresó una letra
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion in palabra_secreta:
                print("¡La letra está en la palabra secreta!")
            else:
                print("La letra no está en la palabra secreta.")
                intentos -= 1
        else:  # Se ingresó una palabra completa
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
            else:
                print("La palabra ingresada no es correcta. Has perdido el juego.")
            break

        if "_" not in palabra_mostrada:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break

    if intentos == 0:
        print("¡Oh no! Has agotado todos tus intentos. Has perdido el juego.")
