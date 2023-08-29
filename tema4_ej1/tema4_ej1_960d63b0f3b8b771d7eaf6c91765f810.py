import random

def ocultar_letras(palabra, cantidad):
    # Generar una lista con los índices de las letras a ocultar
    indices_ocultos = random.sample(range(len(palabra)), cantidad)

    # Reemplazar las letras en los índices ocultos por "_"
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"

    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    # Convertir ambas palabras a listas para facilitar el reemplazo
    lista_palabra_secreta = list(palabra_secreta)
    lista_palabra_mostrada = list(palabra_mostrada)

    # Reemplazar la letra en todas las posiciones que aparece en la palabra
    for i in range(len(lista_palabra_secreta)):
        if lista_palabra_secreta[i] == letra:
            lista_palabra_mostrada[i] = letra

    return "".join(lista_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos_restantes = 7

    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene {} letras y hay {} letras ocultas.".format(len(palabra_secreta), letras_ocultas))

    while intentos_restantes > 0:
        print("\nPalabra actual: {}".format(palabra_mostrada))
        print("Intentos restantes: {}".format(intentos_restantes))

        eleccion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(eleccion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, eleccion)

            if eleccion in palabra_secreta:
                print("¡Letra correcta!")
            else:
                print("Letra incorrecta. ¡Intenta de nuevo!")
                intentos_restantes -= 1

            if palabra_mostrada == palabra_secreta:
                print("\n¡Felicidades! Adivinaste la palabra secreta: {}".format(palabra_secreta))
                break
        elif eleccion == palabra_secreta:
            print("\n¡Felicidades! Adivinaste la palabra secreta: {}".format(palabra_secreta))
            break
        else:
            print("Palabra incorrecta. ¡Intenta de nuevo!")
            intentos_restantes -= 1

    if intentos_restantes == 0:
        print("\nNo adivinaste la palabra secreta. La palabra era: {}".format(palabra_secreta))

