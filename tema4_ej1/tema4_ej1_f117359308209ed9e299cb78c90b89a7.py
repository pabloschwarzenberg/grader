import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta)-1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra contiene", len(palabra_secreta), "letras.")

    while intentos > 0:
        print("\nPalabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        opcion = input("¿Desea ingresar una letra (L) o arriesgar la palabra completa (A)? ").lower()

        if opcion == "l":
            letra = input("Ingrese una letra: ")
            if letra in palabra_secreta:
                palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
                if palabra_mostrada == palabra_secreta:
                    print("¡Felicidades! ¡Has adivinado la palabra secreta!")
                    break
            else:
                print("La letra no se encuentra en la palabra secreta.")
                intentos -= 1
        elif opcion == "a":
            palabra = input("Ingrese la palabra completa: ")
            if palabra == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra secreta!")
            else:
                print("La palabra ingresada no es correcta. La palabra secreta era:", palabra_secreta)
            break
        else:
            print("Opción inválida. Por favor, ingrese 'L' para ingresar una letra o 'A' para arriesgar la palabra completa.")

        if intentos == 0:
            print("¡Oh no! Te has quedado sin intentos. La palabra secreta era:", palabra_secreta)
