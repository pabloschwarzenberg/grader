def ocultar_letras(palabra,cantidad):
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = '_'
    return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = list(palabra_mostrada)
    for indice, caracter in enumerate(palabra_secreta):
        if caracter == letra:
            nueva_palabra_mostrada[indice] = letra
    return ''.join(nueva_palabra_mostrada)



if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "desarrollo", "algoritmo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)-1))
    intentos_restantes = 7
    
    print("Este es el juego de adivinar palabras!")
    print("Adivina la palabra secreta. Tienes", intentos_restantes, "intentos.")
    print("Palabra mostrada:", letras_mostradas)
    
    while intentos_restantes > 0:
        if "_" not in letras_mostradas:
            print("Has adivinado la palabra.")
            break
        
        opcion = input("Ingrese una letra o juegatela adivando la palabra: ")
        
        if len(opcion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
        elif opcion == palabra_secreta:
            print("Has adivinado la palabra completa. Ta bien")
            break
        else:
            print("incorrecto.")
            intentos_restantes -= 1
        
        print("Palabra mostrada:", letras_mostradas)
        print("Intentos restantes:", intentos_restantes)
    
    if intentos_restantes == 0:
        print("Se te acabaron los intentos. Game over")
        print("La palabra era:", palabra_secreta)

         