import random

def ocultar_letras(palabra, cantidad):
    letras = list(palabra)
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    
    for indice in letras_ocultas:
        letras[indice] = "_"
    
    palabra_oculta = "".join(letras)
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "juego", "adivinar"]
    palabra_secreta = random.choice(palabras_secretas)
    
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    
    intentos = 7
    while intentos > 0:
        print("Palabra actual:", palabra_mostrada)
        print("Intentos restantes:", intentos)
        
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        elif opcion == palabra_secreta:
            print("¡Felicitaciones! Has adivinado la palabra.")
            break
        else:
            print("Palabra incorrecta.")
        
        intentos -= 1
    
    if intentos == 0:
        print("¡Lo siento! Has agotado tus intentos. La palabra secreta era:", palabra_secreta)
