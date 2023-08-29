import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada[i] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "mono"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, len(palabra_secreta) // 2)

    intentos = 7
    while intentos > 0:
        print("Palabra actual:",letras_mostradas)
        print(f"Intentos restantes: {intentos}")
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) > 1:
            if opcion == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra.")
                break
            else:
                print("¡Oops! Esa no es la palabra correcta.")
                intentos -= 1
        else:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if letras_mostradas == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra.")
                break
            elif opcion not in palabra_secreta:
                print("¡Letra incorrecta!")
                intentos -= 1

    if intentos == 0:
        print("¡Se acabaron los intentos! La palabra secreta era:", palabra_secreta)
         