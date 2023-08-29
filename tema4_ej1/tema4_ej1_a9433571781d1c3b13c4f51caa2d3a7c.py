import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra[indice] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "leopardo"]
    palabra_secreta = random.choice(palabras_secretas)
    cantidad_letras = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, cantidad_letras)
    
    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras.")
    print("La palabra oculta es:", palabra_mostrada)
    
    intentos = 5
    while intentos > 0:
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            print("La palabra mostrada es:", palabra_mostrada)
            
            if "_" not in palabra_mostrada:
                print("¡Felicitaciones! Has adivinado la palabra secreta:", palabra_secreta)
                break
        else:
            if opcion == palabra_secreta:
                print("¡Felicitaciones! Has adivinado la palabra secreta:", palabra_secreta)
                break
        
        intentos -= 1
        print("Te quedan", intentos, "intentos.")
    
    if "_" in palabra_mostrada:
        print("Lo siento, no has logrado adivinar la palabra secreta. La palabra era:", palabra_secreta)