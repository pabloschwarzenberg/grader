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
    palabras_secretas = ["elefante", "perro", "gato", "leopardo", "rinoceronte"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)

    print("Adivina la palabra secreta")
    print("La palabra tiene", len(palabra_secreta), "letras. Se muestran", letras_mostradas, "letras.")

    intentos = 7
    while intentos > 0:
        print("Palabra:", palabra_oculta)
        respuesta = input("Ingresa una letra o arriésgate con la palabra completa: ")
        if len(respuesta) == 1:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, respuesta)
        elif respuesta == palabra_secreta:
            print("¡Adivinaste la palabra!")
            break
        else:
            print("¡Respuesta incorrecta!")

        intentos -= 1
        if intentos == 0:
            print("¡Se acabaron los intentos!")
            print("La palabra secreta era:", palabra_secreta)
