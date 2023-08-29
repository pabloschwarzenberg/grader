import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    
    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"
    
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_mostrada_lista = list(palabra_mostrada)
    
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_mostrada_lista[i] = letra
    
    return "".join(palabra_mostrada_lista)

if __name__ == "__main__":
    palabras_secretas = ["gato", "perro", "pajaro", "elefante", "jirafa"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7
    
    print("Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene {len(palabra_secreta)} letras. Tienes {intentos} intentos para adivinarla.")
    print("Palabra mostrada: {palabra_mostrada}")
    
    while intentos > 0:
        opcion = input("Ingresa una letra o arriésgate a decir la palabra completa: ")
        
        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            
            if opcion in palabra_secreta:
                print("¡La letra '{opcion}' está en la palabra secreta!")
            else:
                intentos -= 1
                print("La letra '{opcion}' no está en la palabra secreta. Te quedan {intentos} intentos.")
            
            print("Palabra mostrada: {palabra_mostrada}")
            
            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra secreta!")
                break
        else:
            if opcion == palabra_secreta:
                print("¡Felicidades! ¡Has adivinado la palabra secreta!")
                break
            else:
                intentos -= 1
                print("La palabra ingresada no es correcta. Te quedan {intentos} intentos.")
    
    if intentos == 0:
        print("¡Has agotado tus intentos! La palabra secreta era '{palabra_secreta}'. Mejor suerte la próxima vez.")

         