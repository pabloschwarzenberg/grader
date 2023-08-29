import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_secreta = list(palabra_secreta)
    letras_mostradas = list(palabra_mostrada)
    for i in range(len(letras_secreta)):
        if letras_secreta[i] == letra:
            letras_mostradas[i] = letra
    return "".join(letras_mostradas)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "juego"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, int(len(palabra_secreta) * 0.5))
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras y tienes", intentos, "intentos.")

    while intentos > 0:
        print("Palabra:", letras_ocultas)
        opcion = input("Ingresa una letra o escribe 'adivinar' para intentar adivinar la palabra completa: ")

        if opcion == "adivinar":
            palabra_ingresada = input("Ingresa la palabra completa: ")
            if palabra_ingresada == palabra_secreta:
                print("¡Felicitaciones! Adivinaste la palabra correcta.")
                break
            else:
                print("Lo siento, esa no es la palabra correcta.")
                intentos -= 1
        else:
            if len(opcion) != 1:
                print("Ingresa una sola letra.")
                continue
            letras_ocultas = revisar_letra(palabra_secreta, letras_ocultas, opcion)
            if opcion in palabra_secreta:
                print("¡Bien! La letra", opcion, "está en la palabra.")
            else:
                print("La letra", opcion, "no está en la palabra.")
                intentos -= 1

        if "_" not in letras_ocultas:
            print("¡Felicitaciones! Adivinaste la palabra secreta:", palabra_secreta)
            break

    if intentos == 0:
        print("¡Perdiste! No lograste adivinar la palabra secreta:", palabra_secreta)

         