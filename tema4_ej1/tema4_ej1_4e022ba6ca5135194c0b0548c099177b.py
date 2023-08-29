import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_oculta, letra):
    nueva_palabra = list(palabra_oculta)
    
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra[i] = letra
    
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "juego", "computadora"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    
    intentos = 7
    adivinado = False
    
    print("¡Bienvenido al juego de adivinar la palabra!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinar.")
    print("La palabra oculta es:", palabra_oculta)
    print()
    
    while intentos > 0 and not adivinado:
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        opcion = opcion.lower()
        
        if len(opcion) == 1:
            nueva_palabra = revisar_letra(palabra_secreta, palabra_oculta, opcion)
            
            if nueva_palabra == palabra_oculta:
                print("La letra no está en la palabra secreta.")
                intentos -= 1
            else:
                palabra_oculta = nueva_palabra
                print("¡Correcto!")
            
        elif opcion == palabra_secreta:
            adivinado = True
        
        else:
            print("Palabra incorrecta.")
            intentos -= 1
        
        print("Te quedan", intentos, "intentos.")
        print("La palabra oculta es:", palabra_oculta)
        print()
    
    if adivinado:
        print("¡Felicitaciones! Adivinaste la palabra secreta:", palabra_secreta)
    else:
        print("No adivinaste la palabra secreta. Era:", palabra_secreta)
