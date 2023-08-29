import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "videojuego", "internet"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, 3)
    intentos = 7
    
    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("Tienes que adivinar una palabra oculta.")
    print("Puedes ingresar una letra o arriesgarte a decir la palabra completa.")
    print("Tienes", intentos, "intentos para adivinar la palabra.")
    print("La palabra oculta es:", letras_mostradas)
    print()
    
    while intentos > 0:
        if "_" not in letras_mostradas:
            print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
            break
        
        print("Intentos restantes:", intentos)
        opcion = input("Ingresa una letra o la palabra completa: ")
        
        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        elif opcion == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
            break
        else:
            print("Palabra incorrecta. Sigue intentando.")
        
        intentos -= 1
        print("La palabra oculta es:", letras_mostradas)
        print()
    
    if intentos == 0:
        print("¡Lo siento! Te has quedado sin intentos.")
        print("La palabra secreta era:", palabra_secreta)
