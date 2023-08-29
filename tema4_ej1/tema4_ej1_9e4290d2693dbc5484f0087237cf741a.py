import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    
    palabra_oculta = "".join(letras_ocultas)
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_secreta = list(palabra_secreta)
    letras_mostrada = list(palabra_mostrada)
    
    for i in range(len(letras_secreta)):
        if letras_secreta[i] == letra:
            letras_mostrada[i] = letra
    
    palabra_nueva = "".join(letras_mostrada)
    return palabra_nueva

if _name_ == "_main_":
    palabras_secretas = ["python", "programacion", "ordenador", "computadora", "desarrollo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, int(len(palabra_secreta) / 2))

    intentos = 7
    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Intentos restantes:", intentos)
        
        opcion = input("Ingrese una letra o adivine la palabra completa: ")
        
        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        elif len(opcion) > 1:
            if opcion == palabra_secreta:
                letras_mostradas = palabra_secreta
                break
            else:
                print("Palabra incorrecta.")
                intentos -= 1
        else:
            print("Opción inválida. Ingrese una letra o adivine la palabra completa.")
        
        if letras_mostradas == palabra_secreta:
            break
    
    if letras_mostradas == palabra_secreta:
        print("¡Adivinaste la palabra!")
    else:
        print("¡Se acabaron los intentos! La palabra era:", palabra_secreta)