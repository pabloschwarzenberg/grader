import random

def ocultar_letras(palabra, cantidad):
    indices = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for i in indices:
        palabra_oculta[i] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = list(palabra)
    for i, c in enumerate(palabra_secreta):
        if c == letra:
            nueva_palabra[i] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "ornitorrinco", "hipopotamo"]
    palabra_secreta = random.choice(palabras_secretas)
    cantidad_letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_oculta = ocultar_letras(palabra_secreta, cantidad_letras_ocultas)

    intentos = 0
    while intentos < 7:
        print("Palabra:", palabra_oculta)
        adivinanza = input("Ingresa una letra o arriesga la palabra completa: ")
        if adivinanza == palabra_secreta:
            print("¡Ganaste! La palabra secreta era", palabra_secreta)
            break
        elif len(adivinanza) == 1:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, adivinanza)
        else:
            print("Incorrecto")
        intentos += 1

    if intentos == 7:
        print("Perdiste. La palabra secreta era", palabra_secreta)
