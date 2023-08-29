import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    nueva_palabra = list(palabra)

    for indice in letras_ocultas:
        nueva_palabra[indice] = "_"

    return "".join(nueva_palabra)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = list(palabra_mostrada)

    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra[indice] = letra

    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "insecto", "alas", "antenas"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, 3)
    intentos = 7

    while intentos > 0:
        print("Palabra: ",letras_mostradas)
        print("Intentos restantes: ",intentos)
        entrada = input("Ingresa una letra o arriesga la palabra completa: ")

        if len(entrada) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, entrada)

            if entrada in palabra_secreta:
                print("¡Bien! Has acertado una letra.")
            else:
                print("Lo siento, esa letra no está en la palabra.")

            if "_" not in letras_mostradas:
                print("Felicidades, has adivinado la palabra secreta: ",palabra_secreta)
                break
        elif entrada == palabra_secreta:
            print("Felicidades, has adivinado la palabra secreta: ",palabra_secreta)
            break
        else:
            print("Lo siento, esa no es la palabra secreta.")

        intentos -= 1

    if intentos == 0:
        print("No has adivinado la palabra secreta. La palabra era: ",palabra_secreta)

         