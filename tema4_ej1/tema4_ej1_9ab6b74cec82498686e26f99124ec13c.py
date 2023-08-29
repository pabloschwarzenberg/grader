import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = ""
    for i in range(len(palabra)):
        if i in letras_ocultas:
            palabra_oculta += "_"
        else:
            palabra_oculta += palabra[i]
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ""
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]
    return nueva_palabra

if __name__ == "__main__":
    palabras_secretas = ["perro", "gato", "elefante", "jirafa", "rinoceronte"]
    palabra_secreta = random.choice(palabras_secretas)
    cantidad_letras = random.randint(1,len(palabra_secreta))
    palabra_mostrada = ocultar_letras(palabra_secreta,cantidad_letras)
    intentos = 7
    while intentos > 0:
        print("Palabra:",palabra_mostrada)
        letra = input("Ingrese una letra o arriesgue la palabra completa: ")
        if letra == palabra_secreta:
            print("¡Felicidades! Adivinaste la palabra.")
            break
        elif len(letra) > 1:
            print("Lo siento, esa no es la palabra correcta.")
            intentos -= 1
        elif letra in palabra_secreta:
            print("¡Muy bien! La letra está en la palabra.")
            palabra_mostrada = revisar_letra(palabra_secreta,palabra_mostrada,letra)
        else:
            print("Lo siento, esa letra no está en la palabra.")
            intentos -= 1
        if "_" not in palabra_mostrada:
            print("¡Felicidades! Adivinaste la palabra.")
            break
        print("Te quedan",intentos,"intentos.")