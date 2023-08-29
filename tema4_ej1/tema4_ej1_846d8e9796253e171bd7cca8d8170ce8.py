import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
    palabra_mostrada = list(palabra)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_mostrada[i] = letra
    return "".join(palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "insecto", "alas"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    
    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("Tienes 7 intentos para adivinar la palabra.")
    print("La palabra tiene {} letras.".format(len(palabra_secreta)))
    print("Palabra oculta:", palabra_oculta)
    
    intentos = 7
    while intentos > 0:
        print("\nIntentos restantes:", intentos)
        letra_ingresada = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(letra_ingresada) > 1:
            if letra_ingresada == palabra_secreta:
                print("¡Felicidades! ¡Adivinaste la palabra!")
                break
            else:
                print("¡Incorrecto! Esa no es la palabra secreta.")
                intentos -= 1
        else:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, letra_ingresada)
            print("Palabra mostrada:", palabra_oculta)
            
            if palabra_oculta == palabra_secreta:
                print("¡Felicidades! ¡Adivinaste la palabra!")
                break
            
            if letra_ingresada not in palabra_secreta:
                print("¡La letra no está en la palabra secreta!")
                intentos -= 1
    
    if intentos == 0:
        print("¡Oh no! Te quedaste sin intentos. La palabra secreta era:", palabra_secreta)
