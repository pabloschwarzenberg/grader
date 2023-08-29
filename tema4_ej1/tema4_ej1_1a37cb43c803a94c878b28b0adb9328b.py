import random

def ocultar_letras(palabra, cantidad):
    letras_a_ocultar = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)
    for i in letras_a_ocultar:
        palabra_oculta[i] = "_"
    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    palabra_mostrada = list(palabra_mostrada)
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_mostrada[i] = letra
    return "".join(palabra_mostrada)

if __name__ == '__main__':
    palabras_secretas = ['perro', 'gato', 'mono', 'tigre', 'leon']
    palabra_secreta = random.choice(palabras_secretas)
    letras_mostradas = ocultar_letras(palabra_secreta, int(len(palabra_secreta)/2))
    vidas = 7
    while letras_mostradas != palabra_secreta and vidas > 0:
        print('La palabra es:', letras_mostradas)
        print('Tienes', vidas, 'vidas')
        letra = input('Ingresa una letra: ').lower()
        if len(letra) == 1:
            if letra in palabra_secreta:
                letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, letra)
            else:
                vidas -= 1
        else:
            if letra == palabra_secreta:
                letras_mostradas = letra
            else:
                vidas -= 1
    if vidas > 0:
        print('Felicidades, adivinaste la palabra', palabra_secreta)
    else:
        print('Perdiste. La palabra era', palabra_secreta)
