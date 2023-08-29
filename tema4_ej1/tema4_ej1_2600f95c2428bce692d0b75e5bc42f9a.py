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

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "desarrollo"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_mostradas)
    
    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra tiene", len(palabra_secreta), "letras y se muestran", letras_mostradas)
    print("Adivina la palabra o ingresa una letra para descubrir las letras ocultas.")
    
    intentos = 5
    while intentos > 0:
        print("Palabra:", palabra_mostrada)
        
        respuesta = input("Ingresa una letra o la palabra completa: ")
        
        if respuesta == palabra_secreta:
            print("¡Adivinaste la palabra! La palabra secreta era", palabra_secreta)
            break
        elif len(respuesta) == 1:
            letra = respuesta.lower()
            if letra in palabra_secreta:
                palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
                if palabra_mostrada == palabra_secreta:
                    print("¡Adivinaste la palabra! La palabra secreta era", palabra_secreta)
                    break
                else:
                    print("¡Correcto! La letra", letra, "está en la palabra.")
            else:
                print("La letra", letra, "no está en la palabra.")
        else:
            print("Respuesta incorrecta.")
        
        intentos -= 1
        
    if intentos == 0:
        print("No adivinaste la palabra. La palabra secreta era", palabra_secreta)
