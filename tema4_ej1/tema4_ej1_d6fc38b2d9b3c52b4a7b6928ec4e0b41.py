import random

def escoger_palabra():
    palabras = ['python', 'programacion', 'teclado', 'terminal', 'gato', 'perro']
    return random.choice(palabras)

def ocultar_letras(palabra, cantidad):
    letras_ocultas = set(random.sample(range(len(palabra)), cantidad))
    palabra_oculta = list(palabra)
    for i in letras_ocultas:
        palabra_oculta[i] = '_'
    return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_oculta, letra):
    palabra_oculta = list(palabra_oculta)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_oculta[i] = letra
    return ''.join(palabra_oculta)

if __name__ == "__main__":
    palabra_secreta = escoger_palabra()
    cantidad_letras = random.randint(1, len(palabra_secreta)-1)
    palabra_oculta = ocultar_letras(palabra_secreta, cantidad_letras)
    intentos = 7

    while intentos > 0:
        print("Adivina la palabra:", palabra_oculta)
        letra = input('Ingresa una letra o arriesga la palabra completa: ')
        if letra == palabra_secreta:
            print('¡Felicidades, has ganado!')
            break
        elif letra in palabra_secreta:
            palabra_oculta = revisar_letra(palabra_secreta, palabra_oculta, letra)
            if palabra_oculta == palabra_secreta:
                print("Felicidades has ganado La palabra era: ", palabra_secreta)
                break
            else:
                print("Muy bien La letra " ,letra)
        else:
            intentos -= 1
            print("La letra no esta en la palabra. Te quedan", intentos)
            if intentos == 0:
                print("Lo siento has perdido La palabra era" , palabra_secreta)


         