import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)  # Convierte la palabra en una lista de letras
    indices_ocultos = random.sample(range(len(palabra)), cantidad)  # Obtiene índices aleatorios para ocultar letras
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"  # Reemplaza las letras en los índices ocultos por "_"
    return "".join(letras_ocultas)  # Convierte la lista de letras en una cadena nuevamente

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra  # Reemplaza la letra en la posición correspondiente
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]  # Conserva la letra mostrada actualmente
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "libreria", "openai"]
    palabra_secreta = random.choice(palabras_secretas)  # Escoge una palabra secreta aleatoria
    letras_mostradas = ocultar_letras(palabra_secreta, len(palabra_secreta) // 2)  # Oculta la mitad de las letras
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras y tienes", intentos, "intentos.")

    while intentos > 0:
        print("Palabra:", letras_mostradas)

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:  # El jugador ingresó una letra
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)

            if opcion in palabra_secreta:
                print("¡Adivinaste una letra!")
            else:
                intentos -= 1
                print("Letra incorrecta. Te quedan", intentos, "intentos.")

        else:  # El jugador ingresó la palabra completa
            if opcion == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra secreta.")
                break
            else:
                intentos -= 1
                print("Palabra incorrecta. Te quedan", intentos, "intentos.")

    if intentos == 0:
        print("¡Se acabaron tus intentos! La palabra secreta era", palabra_secreta)
