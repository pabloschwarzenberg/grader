import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    n_palabra = list(palabra)
    for indice in letras_ocultas:
        n_palabra[indice] = "_"
    return "".join(n_palabra)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    n_palabra = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            n_palabra[indice] = letra
    return "".join(n_palabra)

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "tortuga"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    
    intentos = 7
    while intentos > 0:
        print("Palabra actual:", palabra_mostrada)
        print("Intentos restantes:", intentos)
        
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
        elif opcion == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra.")
            break
        else:
            print("Palabra incorrecta.")
            intentos -= 1
        
        if palabra_mostrada == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra.")
            break
        
    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)
         