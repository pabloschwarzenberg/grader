import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_oculta, letra):
    palabra_nueva = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_nueva += letra
        else:
            palabra_nueva += palabra_oculta[i]
    return palabra_nueva

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computador", "juego"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = len(palabra_secreta) // 2
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)

    print("¡Bienvenido al juego de adivinar la palabra!")
    print("Palabra oculta:", palabra_oculta)

    while True:
        opcion = input("Ingrese 'l' para ingresar una letra o 'p' para ingresar la palabra completa: ")
        if opcion == "l":
            letra = input("Ingrese una letra: ")
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, letra)
            print("Palabra oculta:", palabra_oculta)
            if palabra_oculta == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra.")
                break
        elif opcion == "p":
            palabra_completa = input("Ingrese la palabra completa: ")
            if palabra_completa == palabra_secreta:
                print("¡Felicidades! Has adivinado la palabra.")
                break
            else:
                print("Palabra incorrecta. Sigue intentando.")
        else:
            print("Opción inválida. Intente de nuevo.")
