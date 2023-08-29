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

def jugar():
    palabras_secretas = ["lepidoptero", "murcielago", "mariposa", "elefante", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos_restantes = 7

    while intentos_restantes > 0:
        print("Palabra actual:", palabra_mostrada)
        print("Intentos restantes:", intentos_restantes)
        print()

        eleccion = raw_input = ("Ingresa una letra o arriésgate con la palabra completa: ")

        if len(eleccion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, eleccion)
        elif eleccion == palabra_secreta:
            print("¡Felicitaciones! Has adivinado la palabra secreta.")
            return
        else:
            print("La palabra ingresada no es correcta.")

        if palabra_mostrada == palabra_secreta:
            print("¡Felicitaciones! Has adivinado la palabra secreta.")
            return

        intentos_restantes -= 1

    print("Oh no, has agotado tus intentos. La palabra secreta era:", palabra_secreta)


#Ejecutar el juego
jugar()