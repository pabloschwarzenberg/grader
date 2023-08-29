import random

def ocultar_letras(palabra, cantidad):
    ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for indice in ocultas:
        palabra_oculta[indice] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_oculta, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_oculta[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["python", "programacion", "computadora", "juego", "adivinar"]
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = random.randint(1, len(palabra_secreta) - 1)
    palabra_oculta = ocultar_letras(palabra_secreta, letras_mostradas)
    intentos = 7

    print("¡Bienvenido al juego de adivinar la palabra secreta!")
    print("La palabra secreta tiene {} letras.".format(len(palabra_secreta)))
    print("Tienes {} intentos para adivinarla.")

    while intentos > 0:
        print("Palabra oculta:", palabra_oculta)
        entrada = input("Ingresa una letra o arriésgate a decir la palabra completa: ")

        if len(entrada) == 1:
            if entrada in palabra_secreta:
                palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, entrada)
                if palabra_oculta == palabra_secreta:
                    print("¡Adivinaste la palabra! Felicitaciones.")
                    break
                else:
                    print("¡Letra encontrada!")
            else:
                print("Letra incorrecta.")
                intentos -= 1
        elif len(entrada) == len(palabra_secreta):
            if entrada == palabra_secreta:
                print("¡Adivinaste la palabra! Felicitaciones.")
                break
            else:
                print("Palabra incorrecta.")
                intentos -= 1
        else:
            print("Entrada inválida. Debes ingresar una letra o la palabra completa.")

        if intentos == 0:
            print("¡Se te acabaron los intentos!")
            print("La palabra secreta era:", palabra_secreta)
