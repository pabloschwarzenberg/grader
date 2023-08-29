import random

def ocultar_letras(palabra, cantidad):
    palabra = list(palabra)
    for _ in range(cantidad):
        i = random.randint(0, len(palabra) - 1)
        palabra[i] = "_"
    return "".join(palabra)

def revisar_letra(palabra_secreta, palabra, letra):
    return "".join(s if s == letra or p != "_" else "_" for s, p in zip(palabra_secreta, palabra))

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "oruga", "caterpillar", "insecto"]
    palabra_secreta = random.choice(palabras_secretas)
    cantidad = random.randint(1, len(palabra_secreta) - 1)
    palabra = ocultar_letras(palabra_secreta, cantidad)

    print("Bienvenido al juego de adivinar la palabra.")
    print("La palabra a adivinar es: ", palabra)

    for i in range(7):
        letra = input("Ingresa una letra o arriesgarte a decir la palabra completa: ")
        if len(letra) > 1:
            if letra == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra.")
                break
            else:
                print("La palabra no es correcta.")
        else:
            palabra = revisar_letra(palabra_secreta, palabra, letra)
            print("La palabra a adivinar es: ", palabra)
            if "_" not in palabra:
                print("¡Felicidades! Has adivinado la palabra.")
                break

    if "_" in palabra:
        print("Lo siento, no has adivinado la palabra. La palabra era: ", palabra_secreta)

         