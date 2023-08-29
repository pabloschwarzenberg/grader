def ocultar_letras(palabra,cantidad):
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_ocultada = list(palabra)
    for indice in indices_ocultos:
        palabra_ocultada[indice] = "_"
    return "".join(palabra_ocultada)

def revisar_letra(palabra_secreta, palabra_ocultada, letra):
    palabra_nueva = list(palabra_ocultada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_nueva[i] = letra
    return "".join(palabra_nueva)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "elefante", "plataforma"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_ocultada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    while intentos > 0:
        print("Palabra ocultada:", palabra_ocultada)
        print("Intentos restantes:", intentos)
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")

        if len(opcion) == 1:
            palabra_ocultada = revisar_letra(palabra_secreta, palabra_ocultada, opcion)
        elif opcion == palabra_secreta:
            print("¡Felicitaciones! Has adivinado la palabra correcta.")
            break
        else:
            print("Palabra incorrecta. ¡Perdiste!")
            break

        if palabra_ocultada == palabra_secreta:
            print("¡Felicitaciones! Has adivinado la palabra correcta.")
            break

        intentos -= 1

    if intentos == 0:
        print("¡Lo siento! Has agotado todos tus intentos. La palabra secreta era:", palabra_secreta)
         