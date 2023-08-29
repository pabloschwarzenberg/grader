def ocultar_letras(palabra,cantidad):
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
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
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "leopardo"]
    palabra_secreta = random.choice(palabras_secretas)

    letras_ocultas = random.randint(1, len(palabra_secreta)-1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)

    intentos = 7
    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! Adivinaste la palabra secreta.")
                break
            else:
                print("La palabra ingresada no es correcta.")

        intentos -= 1

    if intentos == 0:
        print("Se acabaron los intentos. La palabra secreta era:", palabra_secreta)         