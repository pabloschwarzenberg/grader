def ocultar_letras(palabra,cantidad):
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    ocultas = random.sample(range(len(palabra)), cantidad)
    for i in ocultas:
        letras_ocultas[i] = '_'
    return ''.join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ''
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "juego", "adivinar"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta) - 1))
    intentos = 7

    while intentos > 0:
        print("Palabra:", letras_mostradas)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if opcion in palabra_secreta:
                print("¡La letra está en la palabra!")
            else:
                intentos -= 1
                print("La letra no está en la palabra. Te quedan", intentos, "intentos.")
        else:
            if opcion == palabra_secreta:
                print("¡Adivinaste la palabra! ¡Ganaste!")
                break
            else:
                intentos -= 1
                print("La palabra no es correcta. Te quedan", intentos, "intentos.")

    if intentos == 0:
        print("¡Perdiste! La palabra secreta era:", palabra_secreta)
         