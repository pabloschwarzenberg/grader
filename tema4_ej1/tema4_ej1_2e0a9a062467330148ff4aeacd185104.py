import random

def ocultar_letras(palabra, cantidad):
    indices = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for i in indices:
        palabra_oculta[i] = '_'
    return ''.join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra, letra):
    nueva_palabra = list(palabra)
    for i, c in enumerate(palabra_secreta):
        if c == letra:
            nueva_palabra[i] = letra
    return ''.join(nueva_palabra)
import random

palabras_secretas = ['lepidoptero', 'mariposa', 'oruga']
palabra_secreta = random.choice(palabras_secretas)

         