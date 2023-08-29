import random

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
    palabras_secretas = ["perro", "gato", "elefante", "tigre", "leon"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, 2)
    intentos = 7

    print("Bienvenido al juego Adivina la Palabra!")
    print("Adivina la palabra secreta ingresando letras o arriesga la palabra completa.")
    print("Tienes 7 intentos.")

    while intentos > 0:
        print("\nPalabra actual:", letras_mostradas)
        print("Intentos restantes:", intentos)
        eleccion = input("Ingresa una letra o arriesga la palabra completa: ")

        if len(eleccion) == 1:
            letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, eleccion)
            if eleccion not in palabra_secreta:
                intentos -= 1
        else:
            if eleccion == palabra_secreta:
                print("¡Felicitaciones! Adivinaste la palabra secreta:", palabra_secreta)
                break
            else:
                intentos -= 1
        
        if letras_mostradas == palabra_secreta:
            print("¡Felicitaciones! Adivinaste la palabra secreta:", palabra_secreta)
            break

    if intentos == 0:
        print("¡Agotaste tus intentos! La palabra secreta era:", palabra_secreta)