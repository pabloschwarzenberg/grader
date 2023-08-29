import random

def escoger_palabra():
    palabras = ["python", "programacion", "computadora", "desarrollo", "aplicacion"]
    return random.choice(palabras)

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

if _name_ == "_main_":
    palabra_secreta = escoger_palabra()
    letras_mostradas = len(palabra_secreta) // 2  # Mostrar la mitad de las letras
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("Bienvenido/a al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras.")

    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)
        
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion in palabra_secreta:
                print("¡La letra", opcion, "está en la palabra!")
            else:
                print("La letra", opcion, "no está en la palabra.")
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
                break
            else:
                print("La palabra ingresada no es correcta.")

        intentos -= 1

    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)