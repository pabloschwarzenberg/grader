import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra2, letra):
    nueva_palabra_mostrada = list(palabra2)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra_mostrada[indice] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "juego", "computadora", "desarrollo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra2 = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7
    
    print("¡Bienvenido al juego de adivinar palabras!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinarla.")
    print("La palabra mostrada es:", palabra2)
    print()
    
    while intentos > 0:
        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(letra) == 1:
            nueva_palabra_mostrada = revisar_letra(palabra_secreta, palabra2, letra)
            if nueva_palabra_mostrada == palabra2:
                print("La letra no está en la palabra.")
                intentos -= 1
            else:
                palabra2 = nueva_palabra_mostrada
                print("¡Correcto! La letra está en la palabra.")
        elif len(letra) == len(palabra_secreta):
            if letra == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra completa.")
                break
            else:
                print("La palabra completa es incorrecta.")
                intentos -= 1
        else:
            print("Entrada inválida. Por favor, ingresa una letra o la palabra completa.")
        print("Te quedan", intentos, "intentos.")
        print("La palabra mostrada es:", palabra2)
        print()
    
    if intentos == 0:
        print("¡Perdiste! La palabra secreta era:", palabra_secreta)
