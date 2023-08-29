import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_actualizada = list(palabra_mostrada)
    
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            palabra_actualizada[indice] = letra
    
    return "".join(palabra_actualizada)

if __name__ == "__main__":
    palabras_secretas = ["elefante", "guitarra", "programacion", "universidad", "computadora"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta) - 1))
    
    intentos = 7
    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Intentos restantes:", intentos)
        
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        
        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra secreta!")
                break
            else:
                print("La palabra ingresada no es correcta.")
        
        if letras_mostradas == palabra_secreta:
            print("¡Felicidades! ¡Has adivinado la palabra secreta!")
            break
        
        intentos -= 1
    
    if intentos == 0:
        print("¡Se han agotado los intentos! La palabra secreta era:", palabra_secreta)
