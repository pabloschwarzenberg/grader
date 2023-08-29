import random

def ocultar_letras(palabra, cantidad):
    ocultada = list(palabra)
    indices_ocultos = random.sample(range(len(palabra)), cantidad)

    for indice in indices_ocultos:
        ocultada[indice] = '_'

    return ''.join(ocultada)

def revisar_letra(palabra_secreta, palabra_mostrada, letra):
    nueva_palabra = ''

    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra += letra
        else:
            nueva_palabra += palabra_mostrada[i]

    return nueva_palabra

if __name__ == "__main__": 
  palabras_secretas = ['lepidoptero', 'elefante', 'guitarra', 'computadora', 'canguro']
  palabra_secreta = random.choice(palabras_secretas)
  palabra_mostrada = ocultar_letras(palabra_secreta, len(palabra_secreta)//2)

  print('Adivina la palabra secreta: ', palabra_mostrada)

  while True:
        opcion = input('Ingrese una letra o arriesguese a decir la palabra completa: ')

        if len(opcion) == 1:
            palabra_mostrada = revisar_letra(palabra_secreta, palabra_mostrada, opcion)
            print(palabra_mostrada)

            if palabra_mostrada == palabra_secreta:
                print('Felicidades! Has adivinado la palabra secreta.')
                break
        elif opcion == palabra_secreta:
            print('Felicidades! Has adivinado la palabra secreta.')
            break
        else:
            print('Incorrecto! Intentalo nuevamente.')
