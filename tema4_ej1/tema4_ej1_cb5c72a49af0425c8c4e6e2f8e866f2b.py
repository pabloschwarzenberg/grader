#hito 2

import random

palabras_secretas = ["acuerdo", "perro", "estallar", "bandera", "bestia"]

def ocultar_letras(palabra, cantidad):
    reemplazadas = 0
    nueva_cadena = list(palabra)
    while reemplazadas < cantidad:
        pos = random.randint(0, len(palabra) - 1)
        if nueva_cadena[pos] != '_':
            nueva_cadena[pos] = '_'
            reemplazadas = reemplazadas + 1
    return "".join(nueva_cadena)

def revisar_letra(palabra_secreta, palabra, letra):
    if palabra_secreta == letra:
        return palabra_secreta
    else:
        palabra = list(palabra)
        for i in range(0, len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                palabra[i] = letra
        return "".join(palabra)

if __name__ == "__main__":
    intentos = 0
    adivino = 0
    palabra = palabras_secretas[random.randint(0, 4)]
    nueva_palabra = ocultar_letras(palabra, random.randint(1, len(palabra) - 1))

    while intentos < 7:
        print("Palabra secreta: " + nueva_palabra)
        intento = input("Ingrese una letra o la palabra: ")
        intentos = intentos + 1
        nueva_palabra = revisar_letra(palabra, nueva_palabra, intento.lower())
        if nueva_palabra.find("_") == -1:
            adivino = 1
            break

    if adivino == 1:
        print("Felicitaciones! Adivinaste la palabra secreta")
    else:
        print("La palabra secreta era " + palabra + ". Mejor suerte a la proxima!")