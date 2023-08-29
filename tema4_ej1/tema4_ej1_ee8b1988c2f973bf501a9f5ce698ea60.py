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

def main():
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "leon"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)-1))
    intentos = 7
    
    print("Bienvenido al juego de adivinar la palabra secreta.")
    print("Tienes hasta 7 intentos para adivinar la palabra.")
    print("La palabra tiene", len(palabra_secreta), "letras.")
    print("La palabra mostrada es:", letras_mostradas)
    print()
    
    while intentos > 0:
        if "_" not in letras_mostradas:
            print("¡Felicidades! Has adivinado la palabra secreta.")
            break
        
        if intentos == 1:
            print("Último intento...")
        else:
            print("Intentos restantes:", intentos)
        
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(opcion) > 1:
            if opcion == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
            else:
                print("¡Oh no! Esa no es la palabra secreta. La palabra correcta era:", palabra_secreta)
            break
        
        letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        print("La palabra mostrada es:", letras_mostradas)
        print()
        
        intentos -= 1
    
    if intentos == 0:
        print("¡Oh no! Te has quedado sin intentos. La palabra secreta era:", palabra_secreta)

if __name__ == "__main__":
    main()

         