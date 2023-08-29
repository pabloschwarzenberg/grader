import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_mostrada_lista = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_mostrada_lista[i] = letra
    return "".join(palabra_mostrada_lista)

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "leon"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = len(palabra_secreta) // 2
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    while intentos > 0:
        print("Palabra: {}".format(palabra_mostrada))
        print("Intentos restantes: {}".format(intentos))
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        
        if opcion == palabra_secreta:
            print("¡Felicitaciones! Adivinaste la palabra.")
            break
        
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if opcion not in palabra_secreta:
                intentos -= 1
                print("La letra no está en la palabra.")
        else:
            intentos -= 1
            print("La palabra ingresada no es correcta.")

    if intentos == 0:
        print("Lo siento, no lograste adivinar la palabra. La palabra secreta era: {}".format(palabra_secreta))
