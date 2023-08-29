import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for i in letras_ocultas:
        palabra_oculta[i] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = list(palabra)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra[i] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "ordenador", "computadora", "desarrollo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_oculta = ocultar_letras(palabra_secreta, letras_ocultas)
    
    intentos = 7
    while intentos > 0:
        print("Palabra: ", palabra_oculta)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(opcion) > 1:
            if opcion == palabra_secreta:
                print("¡Adivinaste la palabra! La palabra secreta era:", palabra_secreta)
                break
            else:
                print("¡Incorrecto! Esa no es la palabra secreta.")
                intentos -= 1
        else:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, opcion)
            if "_" not in palabra_oculta:
                print("¡Adivinaste la palabra! La palabra secreta era:", palabra_secreta)
                break
            elif opcion not in palabra_secreta:
                print("¡Incorrecto! La letra no se encuentra en la palabra secreta.")
                intentos -= 1
    else:
        print("Se acabaron los intentos. La palabra secreta era:", palabra_secreta)
