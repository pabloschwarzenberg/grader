from os import system
system ("cls")
import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    posiciones_ocultas = random.sample(range(len(letras_ocultas)), cantidad)
    
    for pos in posiciones_ocultas:
        letras_ocultas[pos] = "_"
    
    palabra_oculta = "".join(letras_ocultas)
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_oculta, letra):
    nueva_palabra = ""
    
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_oculta[i]
    
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "algoritmo", "variable"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7
    
    print("Adivina la palabra secreta. Tienes 7 intentos.")
    print("Palabra oculta:", palabra_oculta)
    
    while intentos > 0:
        if "_" not in palabra_oculta:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break
        
        if intentos == 1:
            opcion = input("¡Último intento! ¿Quieres arriesgarte a decir la palabra completa? (s/n): ")
            if opcion.lower() == "s":
                palabra = input("Ingresa la palabra completa: ")
                if palabra == palabra_secreta:
                    print("¡Felicidades! Has adivinado la palabra secreta.")
                else:
                    print("Incorrecto. La palabra secreta era:", palabra_secreta)
                break
        
        letra = input("Ingresa una letra: ")
        palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, letra)
        
        if letra not in palabra_secreta:
            intentos -= 1
            print("Letra incorrecta. Te quedan", intentos, "intentos.")
        
        print("Palabra oculta:", palabra_oculta)
    
    if intentos == 0:
        print("¡Perdiste! La palabra secreta era:", palabra_secreta)
         