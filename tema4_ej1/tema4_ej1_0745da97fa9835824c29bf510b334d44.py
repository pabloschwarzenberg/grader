import random

def ocultar_letras(palabra, cantidad):
    letras = list(palabra)
    ocultas = random.sample(range(len(letras)), cantidad)
    for i in ocultas:
        letras[i] = "_"
    return "".join(letras)

def revisar_letra(palabra_secreta, palabra, letra):
    letras = list(palabra)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            letras[i] = letra
    return "".join(letras)

palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tortuga"]
palabra_secreta = random.choice(palabras_secretas)
letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
palabra = ocultar_letras(palabra_secreta, letras_ocultas)

intentos = 7
while intentos > 0:
    letra = input("Ingresa una letra o intenta adivinar la palabra completa: ")
    if letra == palabra_secreta:
        print("¡Felicidades! Adivinaste la palabra.")
        break
    elif letra in palabra:
        palabra = revisar_letra(palabra_secreta, palabra, letra)
        print("Buena jugada. La palabra es: " + palabra)
        if "_" not in palabra:
            print("¡Felicidades! Adivinaste la palabra.")
            break
    else:
        intentos -= 1
        print("Lo siento, esa letra no está en la palabra. Te quedan " + str(intentos) + " intentos.")

if intentos == 0:
    print("Lo siento, no adivinaste la palabra. Era " + palabra_secreta + ".")