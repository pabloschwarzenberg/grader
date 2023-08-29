import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = '_'
    return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada[i] = letra
    return ''.join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "desarrollo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta) - 1))
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta.")
    print("La palabra secreta tiene {len(palabra_secreta)} letras.")

    while intentos > 0:
        print("\nPalabra actual: {letras_mostradas}")
        print("Intentos restantes: {intentos}")

        entrada = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(entrada) == 1:
            nueva_palabra = revisar_letra(palabra_secreta, letras_mostradas, entrada)
            if nueva_palabra == letras_mostradas:
                print("La letra ingresada no se encuentra en la palabra.")
                intentos -= 1
            else:
                letras_mostradas = nueva_palabra
                if '_' not in letras_mostradas:
                    print("\n¡Felicidades! Has adivinado la palabra secreta: {palabra_secreta}")
                    break
        else:
            if entrada == palabra_secreta:
                print("\n¡Felicidades! Has adivinado la palabra secreta: {palabra_secreta}")
                break
            else:
                print("La palabra ingresada no es correcta.")
                intentos -= 1

    if intentos == 0:
        print("\n¡Oh no! Has agotado todos tus intentos. La palabra secreta era:", palabra_secreta)
