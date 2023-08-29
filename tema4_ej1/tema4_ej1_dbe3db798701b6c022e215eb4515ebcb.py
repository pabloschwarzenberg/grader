import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    letras_a_ocultar = random.sample(range(len(palabra)), cantidad)

    for i in letras_a_ocultar:
        letras_ocultas[i] = "_"

    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_secreta = list(palabra_secreta)
    letras_mostradas = list(palabra_mostrada)

    for i in range(len(letras_secreta)):
        if letras_secreta[i] == letra:
            letras_mostradas[i] = letra

    return "".join(letras_mostradas)

def juego_adivinar_palabra():
    palabras_secretas = ["perro", "gato", "elefante", "tigre", "leon"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)-1))
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene {} letras ocultas: {}".format(len(letras_ocultas), letras_ocultas))

    while intentos > 0:
        if "_" not in letras_ocultas:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            return

        print("Te quedan {} intentos.".format(intentos))
        eleccion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(eleccion) == 1:
            letras_ocultas = revisar_letra(palabra_secreta, letras_ocultas, eleccion)
            print(letras_ocultas)
        else:
            if eleccion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
                return
            else:
                print("Lo siento, esa no es la palabra correcta.")
        
        intentos -= 1

    print("Lo siento, has agotado tus intentos. La palabra secreta era: {}".format(palabra_secreta))

if __name__ == "__main__":
    juego_adivinar_palabra()