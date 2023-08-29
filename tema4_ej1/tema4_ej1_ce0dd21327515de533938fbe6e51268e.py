import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = set()
    while len(letras_ocultas) < cantidad:
        indice = random.randint(0, len(palabra) - 1)
        letras_ocultas.add(indice)
    
    palabra_oculta = ""
    for i in range(len(palabra)):
        if i in letras_ocultas:
            palabra_oculta += "_"
        else:
            palabra_oculta += palabra[i]
    
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabras_secretas = ["lepidoptero", "murcielago", "serpiente", "tortuga", "rinoceronte"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    
    intentos = 7
    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)
        
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
                break
        elif opcion == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra secreta:", palabra_secreta)
            break
        
        intentos -= 1
    
    if intentos == 0:
        print("¡Lo siento! Has agotado tus intentos. La palabra secreta era:", palabra_secreta)
