import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)

    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"

    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = ""

    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra[i]

    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "tigre", "leon"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta)-1)
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)

    intentos = 7
    while intentos > 0:
        print("Palabra: ",palabra_oculta)
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if opcion == palabra_secreta:
            print("¡Felicitaciones! ¡Has adivinado la palabra!")
            break
        elif len(opcion) == 1:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)
            if palabra_oculta == palabra_secreta:
                print("¡Felicitaciones! ¡Has adivinado la palabra!")
                break
        else:
            print("¡Incorrecto!")

        intentos -= 1

    if intentos == 0:
        print("¡Lo siento! Has agotado tus intentos. La palabra secreta era:", palabra_secreta)
