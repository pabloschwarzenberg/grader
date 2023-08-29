import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    
    for indice in indices_ocultos:
        letras_ocultas[indice] = "_"
    
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = list(palabra_mostrada)
    
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra[i] = letra
    
    return "".join(nueva_palabra)

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "murcielago", "mariposa", "insecto"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)-1))
    
    print("Adivina la palabra secreta:")
    print(letras_mostradas)
    
    while True:
        entrada = input("Ingresa una letra o arriesga la palabra completa: ")
        
        if len(entrada) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, entrada)
            print(letras_mostradas)
            
            if "_" not in letras_mostradas:
                print("¡Felicidades! ¡Has adivinado la palabra secreta!")
                break
        elif entrada == palabra_secreta:
            print("¡Felicidades! ¡Has adivinado la palabra secreta!")
            break
        else:
            print("¡Incorrecto! Sigue intentando.")
    