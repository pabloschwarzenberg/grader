import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada[i] = letra
    return "".join(nueva_palabra_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))

    intentos = 7
    while intentos > 0:
        print("Palabra actual:", letras_mostradas)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if opcion == palabra_secreta:
            print("¡Adivinaste la palabra!")
            break

        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
            intentos -= 1
            if "_" not in letras_mostradas:
                print("¡Adivinaste la palabra!")
                break
        else:
            print("La palabra ingresada es incorrecta.")

        print("Intentos restantes:", intentos)
    
    if intentos == 0:
        print("Se acabaron los intentos. La palabra secreta era:", palabra_secreta)
