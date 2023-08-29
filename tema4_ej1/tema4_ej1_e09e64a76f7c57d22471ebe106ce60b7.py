import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_actualizada = list(palabra_mostrada)
    for i, c in enumerate(palabra_secreta):
        if c == letra:
            palabra_actualizada[i] = c
    return "".join(palabra_actualizada)

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tortuga"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene {} letras.".format(len(palabra_secreta)))
    print("Tienes 7 intentos para adivinarla.")

    intentos = 7
    while intentos > 0:
        print("Palabra: ", palabra_mostrada)
        print("Intentos restantes: ", intentos)
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        elif opcion == palabra_secreta:
            palabra_mostrada = opcion
        else:
            print("¡Intento incorrecto!")
            intentos -= 1
        
        if palabra_mostrada == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
            break

    if intentos == 0:
        print("¡Has agotado tus intentos! La palabra secreta era:", palabra_secreta)

         