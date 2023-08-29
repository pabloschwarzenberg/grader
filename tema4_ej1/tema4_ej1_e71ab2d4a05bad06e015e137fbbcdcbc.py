def ocultar_letras(palabra,cantidad):
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
     import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "python", "programacion", "openai", "desafio"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, int(len(palabra_secreta)/2))
    
    intentos = 5
    
    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Tienes", intentos, "intentos restantes.")
        
        opcion = input("¿Deseas ingresar una letra o adivinar la palabra completa? (l/p): ")
        
        if opcion == "l":
            letra = input("Ingresa una letra: ")
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, letra)
        elif opcion == "p":
            palabra = input("Ingresa la palabra completa: ")
            
            if palabra == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra secreta.")
                break
            else:
                print("Palabra incorrecta. Intenta de nuevo.")
                intentos -= 1
        
        print()
    
    if intentos == 0:
        print("Se acabaron los intentos. La palabra secreta era:", palabra_secreta)
    