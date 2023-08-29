import random

def escoger_palabra_secreta(palabras):
    return random.choice(palabras)

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
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
    palabras_secretas = ["python", "programacion", "ordenador", "gato", "libro"]
    palabra_secreta = escoger_palabra_secreta(palabras_secretas)
    letras_ocultas = random.randint(1, len(palabra_secreta) - 1)
    palabra_mostrada = ocultar_letras(palabra_secreta, letras_ocultas)
    
    print("Bienvenido al juego de adivinar la palabra secreta.")
    print(f"La palabra tiene {len(palabra_secreta)} letras. Intenta adivinarla.")
    
    intentos = 7
    while intentos > 0:
        print(f"\nTienes {intentos} intentos restantes.")
        print(f"Palabra actual: {palabra_mostrada}")
        
        opcion = input("¿Deseas ingresar una letra o arriesgar la palabra completa? (letra/palabra): ")
        if opcion == "letra":
            letra = input("Ingresa una letra: ")
            if len(letra) == 1:
                if letra in palabra_secreta:
                    palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, letra)
                    if palabra_mostrada == palabra_secreta:
                        print(f"\n¡Felicidades! Has adivinado la palabra secreta: {palabra_secreta}")
                        break
                    else:
                        print("¡Letra correcta!")
                else:
                    print("Letra incorrecta.")
                    intentos -= 1
            else:
                print("Por favor, ingresa solo una letra.")
        elif opcion == "palabra":
            palabra = input("Ingresa la palabra completa: ")
            if palabra == palabra_secreta:
                print(f"\n¡Felicidades! Has adivinado la palabra secreta: {palabra_secreta}")
                break
            else:
                print("Palabra incorrecta.")
                intentos -= 1
        else:
            print("Opción inválida. Por favor, ingresa 'letra' o 'palabra'.")
    
    if intentos == 0:
        print(f"\nLo siento, has agotado tus intentos. La palabra secreta era: {palabra_secreta}")