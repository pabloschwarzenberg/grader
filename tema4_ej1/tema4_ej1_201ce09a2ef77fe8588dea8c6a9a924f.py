import random

def ocultar_letras(palabra, cantidad):
    letras_ocultas = list(palabra)
    ocultas_indices = random.sample(range(len(letras_ocultas)), cantidad)
    for indice in ocultas_indices:
        letras_ocultas[indice] = '_'
    return ''.join(letras_ocultas)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra_mostrada = ''
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada += letra
        else:
            nueva_palabra_mostrada += palabra_mostrada[i]
    return nueva_palabra_mostrada

palabras_secretas = ['lepidoptero', 'python', 'programacion', 'computadora']
palabra_secreta = random.choice(palabras_secretas)
letras_mostradas = ocultar_letras(palabra_secreta, len(palabra_secreta)//2)

print('Bienvenido al juego de adivinar la palabra secreta!')
print('La palabra secreta tiene', len(palabra_secreta), 'letras.')

while True:
    print('Palabra:', letras_mostradas)
    opcion = input('Ingresa una letra o arriésgate a decir la palabra completa: ')
    
    if len(opcion) == 1:
        letras_mostradas = revisar_letra(palabra_secreta, letras_mostradas, opcion)
    elif opcion == palabra_secreta:
        print('¡Felicidades! Adivinaste la palabra secreta:', palabra_secreta)
        break
    else:
        print('Lo siento, esa no es la palabra secreta.')
    
    if letras_mostradas == palabra_secreta:
        print('¡Felicidades! Adivinaste la palabra secreta:', palabra_secreta)
        break