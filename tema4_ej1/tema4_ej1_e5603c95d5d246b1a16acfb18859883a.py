import random

def escoger_palabra():
    palabras = ["perro", "gato", "elefante", "jirafa", "tigre"]
    return random.choice(palabras)

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
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
    palabra_secreta = escoger_palabra()
    palabra_mostrada = ocultar_letras(palabra_secreta, int(len(palabra_secreta) / 2))
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras y algunas están ocultas.")

    while intentos > 0:
        print("\nPalabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        opcion = input("Ingrese una letra o escriba la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion in palabra_secreta:
                print("¡Letra encontrada!")
            else:
                intentos -= 1
                print("Letra incorrecta. Pierdes 1 intento.")
        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! ¡Has adivinado la palabra secreta!")
                break
            else:
                intentos -= 1
                print("Palabra incorrecta. Pierdes 1 intento.")

    if intentos == 0:
        print("\n¡Has agotado tus intentos! La palabra secreta era:", palabra_secreta)

         