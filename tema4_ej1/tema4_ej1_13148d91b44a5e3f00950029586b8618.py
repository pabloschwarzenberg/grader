import random

# Lista de palabras secretas
palabras_secretas = ["lepidoptero", "mariposa", "insecto", "alas", "polilla"]

def ocultar_letras(palabra, cantidad):
    # Convertir la palabra en una lista de caracteres
    letras = list(palabra)
    # Obtener una lista de índices aleatorios para ocultar letras
    indices_ocultos = random.sample(range(len(letras)), cantidad)
    # Reemplazar las letras en los índices ocultos con "_"
    for indice in indices_ocultos:
        letras[indice] = "_"
    # Convertir la lista de letras nuevamente a una cadena de texto
    palabra_oculta = "".join(letras)
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    # Convertir la palabra secreta y mostrada en listas de caracteres
    secreta = list(palabra_secreta)
    mostrada = list(palabra_mostrada)
    # Reemplazar las letras correspondientes en la palabra mostrada
    for i in range(len(secreta)):
        if secreta[i] == letra:
            mostrada[i] = letra
    # Convertir la lista de letras nuevamente a una cadena de texto
    nueva_palabra_mostrada = "".join(mostrada)
    return nueva_palabra_mostrada

def juego_adivina_palabra():
    # Seleccionar una palabra secreta al azar
    palabra_secreta = random.choice(palabras_secretas)
    # Ocultar algunas letras de la palabra secreta
    palabra_mostrada = ocultar_letras(palabra_secreta, len(palabra_secreta) // 2)
    print("¡Bienvenido al juego de adivinar la palabra!")
    print("Tienes 7 intentos para adivinar la palabra secreta.")
    print("La palabra tiene", len(palabra_secreta), "letras.")
    print("La palabra oculta es:", palabra_mostrada)

    intentos = 7
    while intentos > 0:
        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(letra) == 1:
            nueva_palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
            if nueva_palabra_mostrada == palabra_mostrada:
                print("¡Incorrecto! La letra", letra, "no está en la palabra.")
                intentos -= 1
            else:
                print("¡Correcto! La letra", letra, "está en la palabra.")
                palabra_mostrada = nueva_palabra_mostrada
                if "_" not in palabra_mostrada:
                    print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
                    return
        elif len(letra) == len(palabra_secreta) and letra.lower() == palabra_secreta.lower():
            print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            return
        else:
            print("Entrada inválida. Ingresa una letra o la palabra

         