import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_nueva = list(palabra_mostrada)
    for i, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            palabra_nueva[i] = letra
    return "".join(palabra_nueva)

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "tigre", "leon", "rinoceronte"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7
    
    print("¡Bienvenido al juego de adivinanzas!")
    print("Tienes que adivinar una palabra secreta.")
    print("La palabra tiene",len(palabra_secreta), "letras y",letras_ocultas,"letras están ocultas.")
    print(palabra_mostrada)
    
    while intentos > 0:
        print("\nIntentos restantes:", intentos)
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            print(palabra_mostrada)
            
            if "_" not in palabra_mostrada:
                print("¡Felicidades! Has adivinado la palabra secreta.")
                break
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
                break
        
        intentos -= 1
    
    if intentos == 0:
        print("¡Lo siento! Has agotado todos tus intentos. La palabra secreta era:", palabra_secreta)