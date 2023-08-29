import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    nueva_palabra = ""
    for i in range(len(palabra)):
        if i in indices_ocultos:
            nueva_palabra += "_"
        else:
            nueva_palabra += palabra[i]
    return nueva_palabra

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = len(palabra_secreta) // 2
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)

    intentos = 7
    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion not in palabra_secreta:
                intentos -= 1
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra correctamente.")
                break
            else:
                intentos -= 1
        
        if palabra_mostrada == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra correctamente.")
            break

    if intentos == 0:
        print("Lo siento, te quedaste sin intentos. La palabra secreta era:", palabra_secreta)

         