import random

def ocultar_letras(palabra, cantidad):
    indices_ocultos = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in indices_ocultos:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    return nueva_palabra_mostrada

if __name__ == "__main__":
    palabra_secreta = input("Ingrese la palabra secreta: ")
    letras_ocultas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7
    
    while intentos > 0:
        print("Palabra: ", palabra_mostrada)
        opcion = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        
        if len(opcion) > 1:
            if opcion == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra.")
            else:
                print("¡Incorrecto! La palabra era:", palabra_secreta)
            break
        else:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            
            if palabra_mostrada == palabra_secreta:
                print("¡Felicidades! Adivinaste la palabra.")
                break
            
            intentos -= 1
            if intentos == 0:
                print("Lo siento, has agotado tus intentos. La palabra era:", palabra_secreta)
                break
            else:
                print("Incorrecto. Te quedan", intentos, "intentos.")
