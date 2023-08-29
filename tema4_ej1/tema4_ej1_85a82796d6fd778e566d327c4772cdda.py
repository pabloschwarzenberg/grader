import random

def escoger_palabra_secreta(palabras):
    return random.choice(palabras)

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    ocultas_indices = random.sample(range(len(letras_ocultas)), cantidad)
    for indice in ocultas_indices:
        letras_ocultas[indice] = "_"
    return "".join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "juego", "adivinar"]
    palabra_secreta = escoger_palabra_secreta(palabras_secretas)
    letras_ocultas = ocultar_letras(palabra_secreta, int(len(palabra_secreta)/2))
    intentos = 7
    letras_adivinadas = []
    
    print("Bienvenido al juego de adivinar palabras!")
    print("La palabra secreta tiene", len(palabra_secreta), "letras ocultas.")
    print(letras_ocultas)

    while intentos > 0:
        letra = input("Ingrese una letra o arriésguese a decir la palabra completa: ")
        
        if len(letra) == 1:
            if letra in letras_adivinadas:
                print("Ya has ingresado esa letra. Intenta con otra.")
                continue
            letras_adivinadas.append(letra)
            nueva_palabra = revisar_letra(palabra_secreta, letras_ocultas, letra)
            if nueva_palabra == letras_ocultas:
                intentos -= 1
                print("La letra no está en la palabra. Te quedan", intentos, "intentos.")
            else:
                letras_ocultas = nueva_palabra
                print(letras_ocultas)
                if "_" not in letras_ocultas:
                    print("¡Felicidades! Has adivinado la palabra secreta.")
                    break
        elif len(letra) > 1:
            if letra == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra secreta.")
                break
            else:
                intentos -= 1
                print("La palabra no es correcta. Te quedan", intentos, "intentos.")

    if intentos == 0:
        print("¡Se acabaron los intentos! La palabra secreta era:", palabra_secreta)
