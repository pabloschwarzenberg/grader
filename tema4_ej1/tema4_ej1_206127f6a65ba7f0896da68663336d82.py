import random

def ocultar_letras(palabra, cantidad):
    ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for i in indices_ocultos:
        ocultas[i] = "_"
    return "".join(ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "tigre", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    
    intentos = 7
    while intentos > 0:
        print("Palabra actual:", palabra_mostrada)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        elif opcion == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra secreta.")
            break
        
        if palabra_mostrada == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra secreta.")
            break
        
        intentos -= 1
        print("Intentos restantes:", intentos)
    
    if intentos == 0:
        print("¡Perdiste! La palabra secreta era:", palabra_secreta)
