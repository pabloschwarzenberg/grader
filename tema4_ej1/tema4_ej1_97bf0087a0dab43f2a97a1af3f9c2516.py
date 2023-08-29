import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    palabra_oculta = "".join(letras_ocultas)
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_secreta = list(palabra_secreta)
    letras_mostrada = list(palabra_mostrada)
    for i in range(len(letras_secreta)):
        if letras_secreta[i] == letra:
            letras_mostrada[i] = letra
    nueva_palabra_mostrada = "".join(letras_mostrada)
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["manzana", "perro", "guitarra", "pelota", "avion"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, int(len(palabra_secreta) * 0.4))
    intentos_restantes = 7

    while intentos_restantes > 0:
        print("Palabra: {}".format(letras_mostradas))
        print("Intentos restantes: {}".format(intentos_restantes))

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if opcion not in palabra_secreta:
                intentos_restantes -= 1
        elif len(opcion) > 1:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! Has adivinado la palabra secreta: {}".format(palabra_secreta))
                break
            else:
                print("¡Oops! La palabra ingresada no es correcta.")
                intentos_restantes -= 1
        else:
            print("Ingrese una opción válida.")

        if "_" not in letras_mostradas:
            print("¡Felicitaciones! Has adivinado la palabra secreta: {}".format(palabra_secreta))
            break

    if intentos_restantes == 0:
        print("¡Lo siento! Has agotado tus intentos. La palabra secreta era: {}".format(palabra_secreta))