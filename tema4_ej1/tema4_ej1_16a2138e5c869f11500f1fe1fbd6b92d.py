def ocultar_letras(palabra,cantidad):
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    intentos = 7

    print("Bienvenido al juego de adivinar la palabra secreta.")
    print("La palabra tiene ", len(palabra_secreta), " letras. Adivina qué palabra es.")
    print("Letras mostradas: ", letras_mostradas)

    while intentos > 0:
        print("Intentos restantes:", intentos)
        opcion = input("Ingresa una letra o escribe 'adivinar' para intentar adivinar la palabra completa: ")

        if opcion == "adivinar":
            palabra_intentada = input("Ingresa la palabra completa: ")
            if palabra_intentada == palabra_secreta:
                print("¡Felicitaciones! Adivinaste la palabra correcta.")
                break
            else:
                print("Palabra incorrecta. Sigue intentando.")
                intentos -= 1
        elif len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            print("Letras mostradas:", letras_mostradas)
            if letras_mostradas == palabra_secreta:
                print("¡Felicitaciones! Adivinaste la palabra correcta.")
                break
        else:
            print("Opción inválida. Ingresa una letra o escribe 'adivinar' para intentar adivinar la palabra completa.")

        if intentos == 0:
            print("Se acabaron los intentos. ¡Perdiste!")
            print("La palabra secreta era:", palabra_secreta)
       