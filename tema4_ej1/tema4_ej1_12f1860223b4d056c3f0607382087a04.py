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
    palabras_secretas = ["elefante", "guitarra", "manzana", "programacion", "television"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)

    intentos = 7
    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        opcion = input("Ingrese una letra o arriesgue la palabra completa: ")
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra:", palabra_secreta)
                break
        elif opcion == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra:", palabra_secreta)
            break
        else:
            print("Incorrecto.")
            intentos -= 1
            if intentos == 0:
                print("Lo siento, no lograste adivinar la palabra. La palabra secreta era:", palabra_secreta)
                break
            else:
                print("Te quedan", intentos, "intentos.")
        print()