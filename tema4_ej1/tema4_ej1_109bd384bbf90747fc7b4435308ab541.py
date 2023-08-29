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
    palabras_secretas = ["manzana", "perro", "gato", "elefante", "programacion"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, int(len(palabra_secreta) * 0.3))
    intentos = 7

    print("Adivina la palabra secreta")
    print("Tienes 7 intentos para adivinar")
    print("Palabra:", letras_mostradas)

    while intentos > 0:
        entrada = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(entrada) > 1:
            if entrada == palabra_secreta:
                print("¡Felicitaciones! Adivinaste la palabra secreta:", palabra_secreta)
            else:
                print("Palabra incorrecta. La palabra secreta era:", palabra_secreta)
            break

        if entrada in palabra_secreta:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, entrada)
            print("¡Letra correcta!")
            print("Palabra:", letras_mostradas)
        else:
            print("Letra incorrecta.")
            intentos -= 1
            print("Intentos restantes:", intentos)

        if letras_mostradas == palabra_secreta:
            print("¡Felicitaciones! Adivinaste la palabra secreta:", palabra_secreta)
            break

        if intentos == 0:
            print("¡Agotaste todos los intentos! La palabra secreta era:", palabra_secreta)