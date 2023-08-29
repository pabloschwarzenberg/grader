import random


def crear_lista_palabras():
    lista_palabras = ["gato", "perro", "casa", "carro", "jardín"]
    return lista_palabras


def escoger_palabra(lista_palabras):
    palabra = random.choice(lista_palabras)
    return palabra


def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = ""
    for i in range(len(palabra)):
        if i in letras_ocultas:
            palabra_oculta += "_"
        else:
            palabra_oculta += palabra[i]
    return palabra_oculta


def revisar_letra(palabra_secreta, palabra_oculta, letra):
    nueva_palabra_oculta = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_oculta += letra
        else:
            nueva_palabra_oculta += palabra_oculta[i]
    return nueva_palabra_oculta


if __name__ == "__main__":
    lista_palabras = crear_lista_palabras()
    palabra_secreta = escoger_palabra(lista_palabras)
    palabra_oculta = ocultar_letras(palabra_secreta, 2)
    intentos = 7
    while intentos > 0:
        print("Palabra oculta:", palabra_oculta)
        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if letra == palabra_secreta:
            print("¡Felicidades, ganaste!")
            break
        elif letra in palabra_secreta:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, letra)
            if palabra_oculta == palabra_secreta:
                print("¡Felicidades, ganaste!")
                break
            else:
                print("Letra correcta, sigue intentando.")
        else:
            intentos -= 1
            print("Letra incorrecta, te quedan", intentos, "intentos.")
    if intentos == 0:
        print("¡Lo siento, perdiste! La palabra secreta era:", palabra_secreta)