import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_ocultas = list(palabra_mostrada)
    
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            letras_ocultas[i] = letra
    
    return "".join(letras_ocultas)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "juego", "computadora", "openai"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, len(palabra_secreta) // 2)
    
    intentos = 7
    
    print("¡Bienvenido al juego de adivinar la palabra!")
    print("Tienes 7 intentos para adivinar la palabra secreta.")
    print("Palabra: " + letras_ocultas)
    
    while intentos > 0:
        opcion = input("\nIngrese una letra o arriésguese a decir la palabra completa: ")
        
        if len(opcion) == 1:
            letras_ocultas = revisar_letra(palabra_secreta, letras_ocultas, opcion)
            
            if opcion in letras_ocultas:
                print("¡Bien hecho! La letra está en la palabra.")
            else:
                intentos -= 1
                print("Oops... La letra no está en la palabra. Te quedan {} intentos.".format(intentos))
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra secreta.")
                break
            else:
                intentos -= 1
                print("Oops... Esa no es la palabra secreta. Te quedan {} intentos.".format(intentos))
    
    if intentos == 0:
        print("\n¡Lo siento! Se acabaron los intentos. La palabra secreta era: " + palabra_secreta)
