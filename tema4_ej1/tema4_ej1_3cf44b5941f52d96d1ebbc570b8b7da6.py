import random

def ocultar_letras(palabra, cantidad):
    if cantidad >= len(palabra):
        return '_' * len(palabra)
    else:
        indices_ocultos = random.sample(range(len(palabra)), cantidad)
        palabra_oculta = list(palabra)
        for indice in indices_ocultos:
            palabra_oculta[indice] = '_'
        return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_nueva = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_nueva[i] = letra
    return ''.join(palabra_nueva)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "insecto", "alas", "transformacion"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    print("¡Bienvenido al juego de adivinar palabras!")
    print("La palabra tiene {} letras ocultas.".format(letras_mostradas))
    print("Palabra oculta:", palabra_mostrada)

    while True:
        intento = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(intento) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, intento)
            print("Palabra mostrada:", palabra_mostrada)
            if '_' not in palabra_mostrada:
                print("¡Felicidades! Has adivinado la palabra correctamente.")
                break
        else:
            if intento == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra correctamente.")
                break
            else:
                print("Lo siento, esa no es la palabra correcta. ¡Sigue intentando!")