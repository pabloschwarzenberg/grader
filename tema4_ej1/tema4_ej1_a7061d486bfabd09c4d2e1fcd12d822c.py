import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)

    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"

    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]

    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "pajaro", "elefante", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    cantidad_ocultar = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, cantidad_ocultar)
    print("Adivina la palabra:", palabra_mostrada)

    while True:
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            print("Palabra:", palabra_mostrada)

            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra.")
                break
        elif opcion == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra.")
            break
        else:
            print("Palabra incorrecta. Sigue intentando.")