import random

def ocultar_letras(palabra, cantidad):
    palabra_oculta = list(palabra)
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = list(palabra_mostrada)
    
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra[indice] = letra
    
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "juego", "gato"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)-1))
    intentos = 7
    
    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    
    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Intentos restantes:", intentos)
        
        opcion = input("Ingrese una letra o arriesgue la palabra completa: ")
        
        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Adivinaste la palabra! ¡Has ganado!")
                break
            else:
                print("¡Palabra incorrecta! Sigue intentando.")
        
        intentos -= 1
    
    if intentos == 0:
        print("¡Se acabaron los intentos! La palabra secreta era:", palabra_secreta)
