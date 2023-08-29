import random

def ocultar_letras(palabra, cantidad):
    ocultas = list(palabra)
    indices = random.sample(range(len(palabra)), cantidad)
    for i in indices:
        ocultas[i] = '_'
    return ''.join(ocultas)

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = ''
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ['lepidoptero', 'mariposa', 'insecto', 'oruga', 'pupa']
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene {} letras. Buena suerte!".format(len(palabra_secreta)))

    while intentos > 0:
        print("\nPalabra actual: {}".format(palabra_oculta))
        print("Intentos restantes: {}".format(intentos))

        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) > 1:
            if opcion == palabra_secreta:
                print("\nFelicitaciones, has adivinado la palabra secreta: {}".format(palabra_secreta))
            else:
                print("\nLo siento, esa no es la palabra secreta. La palabra correcta era: {}".format(palabra_secreta))
            break

        if opcion in palabra_secreta:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)
            if palabra_oculta == palabra_secreta:
                print("\nFelicitaciones, has adivinado la palabra secreta: {}".format(palabra_secreta))
                break
            else:
                print("\n¡Muy bien! La letra '{}' está en la palabra secreta.".format(opcion))
        else:
            print("\nLo siento, la letra '{}' no está en la palabra secreta.".format(opcion))
            intentos -= 1

    if intentos == 0:
        print("\n¡Se te acabaron los intentos! La palabra secreta era: {}".format(palabra_secreta))
