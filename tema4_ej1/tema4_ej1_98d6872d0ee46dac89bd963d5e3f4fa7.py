import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tortuga"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))

    intentos = 7
    while intentos > 0:
        print("Palabra:", letras_mostradas)
        print("Intentos restantes:", intentos)

        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        
        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra secreta.")
                break
            else:
                print("Lo siento, la palabra ingresada no es correcta.")
                intentos -= 1
        
        if letras_mostradas == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra secreta.")
            break
    
    if intentos == 0:
        print("No lograste adivinar la palabra secreta. La palabra era:", palabra_secreta)
