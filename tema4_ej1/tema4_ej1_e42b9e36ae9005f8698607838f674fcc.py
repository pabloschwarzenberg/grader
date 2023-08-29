import random
import sys


def ocultar_letras(palabra, cantidad):
    incognitas = random.sample(range(0, len(palabra)), cantidad)
    palabra_lista = list(palabra)
    for i in incognitas:
        palabra_lista[i] = '_'
    return ''.join(palabra_lista)


def revisar_letra(palabra_secreta, palabra, letra):
    i = 0
    palabra_lista = list(palabra)
    while i < len(palabra):
        if palabra[i] == '_' and palabra_secreta[i] == letra:
            palabra_lista[i] = letra
        i += 1
    return ''.join(palabra_lista)


if __name__ == "__main__":
    palabras = ['velociraptor', 'paralelepipedo', 'ciclopentanoperhidrofenantreno', 'vagina', 'comunismo',
                'capitalismo', 'drogas', 'paracetamol', 'fosfatidilcolina']
    escogida = random.choice(palabras)
    actual = ocultar_letras(escogida, random.randrange(0, len(escogida)) - 1)
    intento = 0
    print('¡Adivina esta palabra, si puedes!')
    print(actual.upper())
    while actual.find('_') != -1:
        TempA = input('Ingresa una letra: ')
        TempB = revisar_letra(escogida, actual, TempA)
        if actual == TempB:
            print('¡Fallaste!')
            intento += 1
            if intento >= 7:
                print('¡Se acabó!  No lograste adivinar la palabra. Era')
                print(escogida.upper())
                print('¡¿Cómo no catchái?!')
                sys.exit(0)
        actual = TempB
        print(actual.upper())
