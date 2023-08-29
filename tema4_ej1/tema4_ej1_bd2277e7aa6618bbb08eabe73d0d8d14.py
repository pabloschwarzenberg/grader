import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    
    for indice in indices_ocultos:
        letras_ocultas[indice] = '_'
    
    return ''.join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    letras_mostradas = list(palabra_mostrada)
    
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            letras_mostradas[i] = letra
    
    return ''.join(letras_mostradas)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "mariposa", "insecto", "alas"]
    palabra_secreta = random.choice(palabras_secretas)
    
    letras_ocultas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    print("Adivina la palabra:", letras_ocultas)
    
    intentos = 7
    while intentos > 0:
        entrada = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(entrada) > 1:
            if entrada == palabra_secreta:
                print("¡Correcto! ¡Has adivinado la palabra!")
                break
            else:
                print("Incorrecto. Intenta de nuevo.")
        else:
            letras_mostradas = revisar_letra(palabra_secreta, letras_ocultas, entrada)
            if letras_mostradas == letras_ocultas:
                intentos -= 1
                print("La letra '{}' no está en la palabra. Te quedan {} intentos.".format(entrada, intentos))
            else:
                letras_ocultas = letras_mostradas
                print("¡Correcto! La palabra ahora es:", letras_ocultas)
                
        if intentos == 0:
            print("¡Se acabaron los intentos! La palabra era:", palabra_secreta)
