import random

def ocultar_letras(palabra, cantidad):
    # Convertir la palabra en una lista de caracteres
    letras = list(palabra)

    # Obtener la longitud de la palabra
    longitud = len(palabra)

    # Generar una lista de índices aleatorios para ocultar las letras
    indices_ocultos = random.sample(range(longitud), cantidad)

    # Ocultar las letras en los índices seleccionados
    for indice in indices_ocultos:
        letras[indice] = "_"

    # Convertir la lista de caracteres de nuevo a una cadena de texto
    palabra_oculta = "".join(letras)

    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    # Convertir la palabra secreta y la palabra mostrada en listas de caracteres
    letras_secretas = list(palabra_secreta)
    letras_mostradas = list(palabra_mostrada)

    # Verificar si la letra está en la palabra secreta
    if letra in letras_secretas:
        # Reemplazar la letra en todas las posiciones correspondientes en la palabra mostrada
        for i in range(len(letras_secretas)):
            if letras_secretas[i] == letra:
                letras_mostradas[i] = letra

    # Convertir las listas de caracteres de nuevo a cadenas de texto
    palabra_nueva = "".join(letras_mostradas)

    return palabra_nueva

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "rinoceronte"]
    palabra_secreta = random.choice(palabras_secretas)

    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)-1))
    intentos = 7

    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Intentos restantes:", intentos)

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra.")
                break
            else:
                print("La palabra ingresada no es correcta.")

        intentos -= 1

    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra correcta era:", palabra_secreta)

         