import random

# Lista de palabras secretas
palabras_secretas = ["gato", "perro", "elefante", "jirafa", "leon", "tigre", "mono", "rinoceronte"]

# Función para ocultar letras en la palabra secreta
def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

# Función para revisar si una letra existe en la palabra secreta
def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    return nueva_palabra_mostrada

if __name__ == "__main__":
    # Escoger una palabra secreta aleatoria
    palabra_secreta = random.choice(palabras_secretas)
    num_letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, num_letras_mostradas)

    # Variables de juego
    intentos = 7
    letras_intentadas = []

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras. Adivina la palabra antes de que se te acaben los intentos.")

    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)
        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ").lower()

        if len(letra) == 1:
            if letra in letras_intentadas:
                print("Ya has intentado con esa letra. ¡Intenta con otra!")
                continue
            letras_intentadas.append(letra)
            if letra in palabra_secreta:
                palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
                if palabra_mostrada == palabra_secreta:
                    print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
                    break
                print("¡Bien hecho! La letra", letra, "está en la palabra.")
            else:
                intentos -= 1
                print("La letra", letra, "no está en la palabra. Intenta nuevamente.")
        else:
            if letra == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
                break
            else:
                intentos -= 1
                print("La palabra ingresada no es correcta. Intenta nuevamente.")

    if intentos == 0:
        print("¡Oh no! Te has quedado sin intentos. La palabra secreta era", palabra_secreta)

         