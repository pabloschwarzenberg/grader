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
    palabras_secretas = ["gato", "perro", "elefante", "jirafa", "tigre"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, random.randint(1, len(palabra_secreta)))
    print("¡Adivina la palabra secreta!")
    print(f"Palabra: {letras_mostradas}")

    intentos = 7
    while intentos > 0:
        if "_" not in letras_mostradas:
            print("¡Has adivinado la palabra!")
            break

        if intentos == 1:
            opcion = input("¿Quieres arriesgarte a decir la palabra completa? (s/n): ")
            if opcion.lower() == "s":
                palabra_completa = input("Ingresa la palabra completa: ")
                if palabra_completa == palabra_secreta:
                    print("¡Has adivinado la palabra!")
                else:
                    print("¡Incorrecto! Has agotado tus intentos.")
                break

        letra = input("Ingresa una letra: ")
        letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, letra)
        print(f"Palabra: {letras_mostradas}")
        intentos -= 1

    if intentos == 0:
        print("¡Has agotado tus intentos! La palabra secreta era:", palabra_secreta)
