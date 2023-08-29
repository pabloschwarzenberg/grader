import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    nueva_palabra = list(palabra)
    for indice in letras_ocultas:
        nueva_palabra[indice] = "_"
    return "".join(nueva_palabra)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra[i] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "aprendizaje", "desarrollo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)

    intentos = 7
    while intentos > 0:
        print("Palabra: {palabra_mostrada}")
        intento = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(intento) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, intento)
        else:
            if intento == palabra_secreta:
                print("¡Adivinaste la palabra!")
                break
            else:
                print("Palabra incorrecta.")
        
        if palabra_mostrada == palabra_secreta:
            print("¡Felicidades, adivinaste la palabra secreta!")
            break
        
        intentos -= 1

    if intentos == 0:
        print(f"Se te acabaron los intentos. La palabra secreta era: {palabra_secreta}")
