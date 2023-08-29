import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "juego", "desafio"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    
    intentos = 7
    
    print("Bienvenido al juego de adivinar la palabra secreta.")
    print("Tienes 7 intentos para adivinar la palabra.")
    print("La palabra contiene", len(palabra_secreta), "letras.")
    print("Palabra:", letras_mostradas)
    
    while intentos > 0:
        if "_" not in letras_mostradas:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break
        
        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(letra) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, letra)
            print("Palabra:", letras_mostradas)
        elif len(letra) == len(palabra_secreta) and letra == palabra_secreta:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break
        else:
            print("Palabra incorrecta.")
        
        intentos -= 1
    
    if intentos == 0:
        print("Lo siento, has agotado todos tus intentos. La palabra secreta era:", palabra_secreta)