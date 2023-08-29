import random

def ocultar_letras(palabra, cantidad):
    if cantidad >= len(palabra):
        return "_" * len(palabra)
    else:
        indices_ocultos = random.sample(range(len(palabra)), cantidad)
        palabra_oculta = list(palabra)
        for indice in indices_ocultos:
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
    palabras_secretas = ["lepidoptero", "mariposa", "oruga", "polilla"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))

    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    print("Palabra oculta:", palabra_oculta)

    intentos = 7
    while intentos > 0:
        if "_" not in palabra_oculta:
            print("¡Felicitaciones! Has adivinado la palabra.")
            break

        opcion = input("Ingrese una letra o adivine la palabra completa: ")

        if len(opcion) == 1:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! Has adivinado la palabra.")
                break
            else:
                print("La palabra ingresada no es correcta.")

        intentos -= 1

    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)
