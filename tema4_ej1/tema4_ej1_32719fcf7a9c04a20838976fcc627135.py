import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
    palabra_actualizada = list(palabra)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_actualizada[i] = letra
    return "".join(palabra_actualizada)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "teclado", "openai"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))

    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    print("Adivina la palabra secreta:")
    print(palabra_oculta)

    intentos = 7
    while intentos > 0:
        letra = input("Ingresa una letra o arriesga la palabra completa: ")
        if letra == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra secreta.")
            break
        elif len(letra) == 1:
            palabra_actualizada = revisar_letra(palabra_secreta, palabra_oculta, letra)
            if palabra_actualizada == palabra_oculta:
                intentos -= 1
                print("Letra incorrecta. Te quedan", intentos, "intentos.")
            else:
                palabra_oculta = palabra_actualizada
                print(palabra_oculta)
                if "_" not in palabra_oculta:
                    print("¡Felicidades! Adivinaste la palabra secreta.")
                    break
        else:
            intentos -= 1
            print("Palabra incorrecta. Te quedan", intentos, "intentos.")

    if intentos == 0:
        print("¡Oh no! Se acabaron los intentos. La palabra secreta era:", palabra_secreta)
         