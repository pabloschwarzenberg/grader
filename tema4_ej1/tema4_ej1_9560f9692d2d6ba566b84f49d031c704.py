
from random import choice, randint

def ocultar_letras(palabra_secreta, numero_letras):
    indices_ocultos = set()
    while len(indices_ocultos)<numero_letras:
        indices_ocultos.add(randint(0, len(palabra_secreta)-1))
    palabra = [char for char in palabra_secreta]
    for ix in indices_ocultos:
        palabra[ix] = '_'
    return ''.join(palabra)

def revisar_letra(palabra_secreta, palabra, letra):
    if letra not in palabra_secreta:
        return palabra
    palabra = [char for char in palabra]
    for ix in range(len(palabra_secreta)):
        if palabra_secreta[ix] == letra:
            palabra[ix] = letra
    return ''.join(palabra)


if __name__ == '__main__':
    secret = ['lepidoptero', 'paralelepipedo', 'murcielago', 'mamifero', 'hipopotamo', 'perro', 'helicoptero', 'libelula', 'tomate']
    palabra_secreta = choice(secret)
    numero_letras = randint(1, len(palabra_secreta)-1)
    palabra = ocultar_letras(palabra_secreta, numero_letras)
    #print(f'(TEST) La palabra secreta es: {palabra_secreta}, y la palabra oculta es {palabra}')
    letra = input('(TEST) Ingrese una letra a revisar: ')
    #print(f'(TEST) La palabra ya fue revisada, y retornó: {revisar_letra(palabra_secreta, palabra, letra)}')
