import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"

    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_secreta = list(palabra_secreta)
    palabra_mostrada = list(palabra_mostrada)

    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_mostrada[i] = letra

    return "".join(palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "algoritmo", "variable"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, int(len(palabra_secreta)/2))
    
    intentos = 7
    palabra_mostrada = letras_ocultas

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("Tienes 7 intentos para adivinar la palabra.")
    print("La palabra secreta tiene {len(palabra_secreta)} letras y algunas están ocultas.")

    while intentos > 0:
        print("\nPalabra actual:", palabra_mostrada)
        print("Intentos restantes: {intentos}")
        
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion in palabra_secreta:
                print("¡Letra correcta!")
            else:
                intentos -= 1
                print("Letra incorrecta. Pierdes un intento.")
        elif opcion == palabra_secreta:
            print("¡Felicitaciones! ¡Has adivinado la palabra secreta!")
            break
        else:
            intentos -= 1
            print("Palabra incorrecta. Pierdes un intento.")

    if intentos == 0:
        print("\n¡Oh no! Has agotado todos tus intentos.")
        print("La palabra secreta era: {palabra_secreta}")
