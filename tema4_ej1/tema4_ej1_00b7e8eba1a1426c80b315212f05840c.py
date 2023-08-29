import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "tortuga", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    intentos = 7

    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Intentos restantes",intentos)

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) > 1:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! ¡Has adivinado la palabra!")
            else:
                print("¡Oops! La palabra correcta era", {palabra_secreta}, " ¡Has perdido!")
            break

        if opcion in palabra_secreta:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if letras_mostradas == palabra_secreta:
                print("¡Felicitaciones! ¡Has adivinado la palabra!")
                break
        else:
            print("La letra no está en la palabra secreta.")
            intentos -= 1

        print()

    if intentos == 0:
        print("¡Oops! La palabra correcta era", palabra_secreta, " ¡Has perdido!")

         