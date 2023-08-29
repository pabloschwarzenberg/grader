import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = '_'
    return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra[i] = letra
    return ''.join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "murcielago", "ornitorrinco", "hipopotamo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    print("¡Adivina la palabra secreta!")
    print("Palabra mostrada:", palabra_mostrada)
    
    while True:
        entrada = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(entrada) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, entrada)
            print("Palabra mostrada:", palabra_mostrada)
            
            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
                break
        else:
            if entrada == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
                break
            else:
                print("Palabra incorrecta. Sigue intentando.")

         