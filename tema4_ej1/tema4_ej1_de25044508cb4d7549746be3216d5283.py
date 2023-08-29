def numero_perfecto(numero):
    suma_divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma_divisores += divisor
    return suma_divisores == numero
if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    if numero_perfecto(numero):
        print("El número es perfecto")
    else:
        print("El número no es perfecto")
        
#ADIVINA LA PALABRA
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

    intentos = 0
    while intentos < 7:
        entrada = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        if len(entrada) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, entrada)
            print("La palabra mostrada es:", palabra_mostrada)
        else:
            if entrada == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra correcta.")
                break
            else:
                print("Lo siento, esa no es la palabra correcta.")
        intentos += 1
    else:
        print("¡Perdiste! Se te acabaron los intentos. La palabra secreta era:", palabra_secreta)
         