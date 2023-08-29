import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for i in letras_ocultas:
        palabra_oculta[i] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_mostrada[i] = letra
    return "".join(palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "computadora", "elefante", "programacion", "guitarra"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta)-1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    
    intentos = 7
    while intentos > 0:
        print("Palabra actual:", palabra_mostrada)
        
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        
        if opcion == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra correctamente.")
            break
        elif len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra correctamente.")
                break
        else:
            print("Esa no es la palabra correcta.")
        
        intentos -= 1
        print("Intentos restantes:", intentos)
        
    if intentos == 0:
        print("¡Se acabaron los intentos! La palabra secreta era:", palabra_secreta)
         