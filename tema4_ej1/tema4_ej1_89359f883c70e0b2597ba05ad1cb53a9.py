import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_secreta = list(palabra_secreta)
    letras_mostrada = list(palabra_mostrada)
    for i in range(len(letras_secreta)):
        if letras_secreta[i] == letra:
            letras_mostrada[i] = letra
    return "".join(letras_mostrada)

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "pajaro", "elefante", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, int(len(palabra_secreta)/2))
    intentos = 7
    
    while intentos > 0:
        print("Palabra:", letras_ocultas)
        print("Intentos restantes:", intentos)
        
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(opcion) == 1:
            letras_ocultas = revisar_letra(palabra_secreta, letras_ocultas, opcion)
        elif opcion == palabra_secreta:
            print("¡Adivinaste!")
            break
        else:
            print("Incorrecto")
            intentos -= 1
        
        if "_" not in letras_ocultas:
            print("¡Adivinaste!")
            break
    
    if "_" in letras_ocultas:
        print("No adivinaste. La palabra era:", palabra_secreta)
  