import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "tigre", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)-1))
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print(f"La palabra secreta tiene {len(palabra_secreta)} letras.")
    print(letras_mostradas)

    while intentos > 0:
        if "_" not in letras_mostradas:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break

        opcion = input("Ingresa una letra o arriesga la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            print(letras_mostradas)
        elif opcion == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break
        else:
            print("La palabra ingresada no es correcta.")

        intentos -= 1

    if "_" in letras_mostradas:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)