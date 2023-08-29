import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra[i] = letra
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "insecto", "alas"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7
    
    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras.")
    print("Tienes", intentos, "intentos para adivinar la palabra.")
    print("Palabra mostrada:", palabra_mostrada)
    
    while intentos > 0:
        print()
        letra_o_palabra = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(letra_o_palabra) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra_o_palabra)
            print("Palabra mostrada:", palabra_mostrada)
            
            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
                break
        else:
            if letra_o_palabra == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
                break
        
        intentos -= 1
        print("Intentos restantes:", intentos)
    
    if intentos == 0:
        print("¡Lo siento! Has agotado todos tus intentos. La palabra secreta era:", palabra_secreta)
         