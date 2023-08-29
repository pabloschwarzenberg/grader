import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra_mostrada[indice] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "oruga", "pupa", "antenas"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)

    print("¡Bienvenido al juego de adivinar la palabra!")
    print("Tienes hasta 7 intentos para adivinar la palabra.")
    print("La palabra mostrada es:", palabra_mostrada)