import random
def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = ""
    
    for i in range(len(palabra)):
        if i in letras_ocultas:
            palabra_oculta += "_"
        else:
            palabra_oculta += palabra[i]
    
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

def jugar():
    palabras_secretas = ["python", "programacion", "computadora", "desarrollo", "juego"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras.")

    while intentos > 0:
        print("\nPalabra:", letras_mostradas)
        print("Intentos restantes:", intentos)
        
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            if opcion in palabra_secreta:
                print("¡Letra correcta!")
            else:
                print("Letra incorrecta.")
                intentos -= 1
        else:
            if opcion == palabra_secreta:
                print("¡Adivinaste la palabra! ¡Ganaste!")
                return
            else:
                print("Palabra incorrecta.")
                intentos -= 1
    
    print("\n¡Se acabaron los intentos! La palabra secreta era:", palabra_secreta)
    print("¡Perdiste!")

if __name__ == "__main__":
    jugar()
