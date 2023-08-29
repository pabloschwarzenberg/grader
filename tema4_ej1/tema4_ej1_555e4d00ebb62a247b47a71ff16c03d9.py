import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_mostrada[i] = letra
    return "".join(palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "desarrollo", "openai"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    
    intentos = 7
    while intentos > 0:
        print("Palabra mostrada:", letras_mostradas)
        print("Intentos restantes:", intentos)
        
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        
        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        elif opcion == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra correctamente.")
            break
        else:
            print("Lo siento, esa no es la palabra correcta.")
            intentos -= 1
        
        if "_" not in letras_mostradas:
            print("¡Felicidades! Has adivinado la palabra correctamente.")
            break
        
    if intentos == 0:
        print("¡Has agotado todos tus intentos! La palabra secreta era:", palabra_secreta)