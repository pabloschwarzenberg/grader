import random

def ocultar_letras(palabra, cantidad):
    indices = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for i in indices:
        palabra_oculta[i] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = list(palabra)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra[i] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "ornitorrinco", "hipopotamo"]
    palabra_secreta = random.choice(palabras_secretas)
    cantidad_letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_oculta = ocultar_letras(palabra_secreta, cantidad_letras_ocultas)

    intentos = 7
    while intentos > 0:
        intentos -= 1
        print("Palabra:", palabra_oculta)
        adivinanza = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if adivinanza == palabra_secreta:
            print("Adivinaste, la palabra era", palabra_secreta)
            break
        elif len(adivinanza) == 1:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, adivinanza)
        else:
            print("No es la palabra correcta")

    if intentos == 0:
        print("No adivinaste, la palabra era", palabra_secreta)