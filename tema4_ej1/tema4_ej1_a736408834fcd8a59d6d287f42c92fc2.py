import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    letras_mostradas = []
    
    # Generar una lista de posiciones aleatorias para ocultar letras
    posiciones_ocultas = random.sample(range(len(palabra)), cantidad)
    
    # Reemplazar las letras en las posiciones ocultas por "_"
    for pos in posiciones_ocultas:
        letras_ocultas[pos] = "_"
    
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
    palabras_secretas = ["perro", "gato", "elefante", "tigre", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    intentos = 7
    
    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras.")
    print(letras_mostradas)
    
    while intentos > 0:
        if "_" not in letras_mostradas:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break
        
        letra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(letra) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, letra)
            intentos -= 1
        elif letra == palabra_secreta:
            letras_mostradas = palabra_secreta
            break
        else:
            print("¡La palabra ingresada no es correcta!")
            intentos -= 1
        
        print(letras_mostradas)
    
    if "_" in letras_mostradas:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)
