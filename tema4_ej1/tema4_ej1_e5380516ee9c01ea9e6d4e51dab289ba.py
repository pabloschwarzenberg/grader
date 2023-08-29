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
    palabras_secretas = ["python", "programacion", "computadora", "juego", "divertido"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)-1))
    
    intentos = 7
    adivinado = False
    
    print("¡Bienvenido al juego de adivinar la palabra!")
    print("Tienes 7 intentos para adivinar la palabra secreta.")
    
    while intentos > 0:
        print("Palabra:", letras_ocultas)
        print("Intentos restantes:", intentos)
        
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        
        if len(opcion) == 1:
            letras_ocultas = revisar_letra(palabra_secreta, letras_ocultas, opcion)
        else:
            if opcion == palabra_secreta:
                adivinado = True
                break
        
        if palabra_secreta == letras_ocultas:
            adivinado = True
            break
        
        intentos -= 1
    
    if adivinado:
        print("¡Felicidades! Adivinaste la palabra secreta:", palabra_secreta)
    else:
        print("No adivinaste la palabra secreta. La palabra era:", palabra_secreta)
    
    print("¡Gracias por jugar!")
