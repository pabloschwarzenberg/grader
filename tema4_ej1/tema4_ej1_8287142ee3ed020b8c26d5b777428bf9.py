import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
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
    palabras_secretas = ["manzana", "banana", "naranja", "pera", "uva"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    
    intentos = 7
    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        letra = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        if len(letra) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
        else:
            if letra == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
                break
        intentos -= 1
        print("Intentos restantes:", intentos)
    
    if intentos == 0:
        print("Lo siento, has agotado tus intentos. La palabra secreta era:", palabra_secreta)
