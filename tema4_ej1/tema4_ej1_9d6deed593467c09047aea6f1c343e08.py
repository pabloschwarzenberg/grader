import random
palabras_secretas = ["manzana", "perro", "computadora", "bicicleta", "jirafa", "cocodrilo", "television"]
palabra_secreta = random.choice(palabras_secretas)
letras_ocultas = random.randint(1, len(palabra_secreta)//2)

def ocultar_letras(palabra, cantidad):
    posiciones_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = ""
    for i in range(len(palabra)):
        if i in posiciones_ocultas:
            palabra_oculta += "_"
        else:
            palabra_oculta += palabra[i]
    return palabra_oculta

    palabra_oculta = ocultar_letras(palabra_secreta, letras_ocultas)
    intentos = 7

    while intentos > 0 and palabra_secreta != palabra_oculta:
        print("Palabra: ",palabra_oculta)
        letra = input("Ingresa una letra o arriesga a decir la palabra completa: ")
        if len(letra) == 1:
            if letra in palabra_secreta:
                palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, letra)
            else:
                print("Letra incorrecta. Pierdes un intento.")
            intentos -= 1
        else:
            if letra == palabra_secreta:
                print("Felicitaciones, ganaste!")
                break
            else:
                print("Palabra incorrecta. Pierdes un intento.")
            intentos -= 1

    if intentos == 0:
        print("Lo siento, perdiste.")
        print("La palabra era ",palabra_secreta)

def revisar_letra(palabra_secreta, palabra_oculta, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_oculta[i]
    return nueva_palabra