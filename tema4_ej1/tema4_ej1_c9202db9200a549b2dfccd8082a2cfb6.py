#imports
from random import randint
#F2: ocultar letras
def ocultar_letras(palabraSecreta, cantLetrasOcultar):
    lisposiOcultar = []
    numeros = 0
    secuencia = ''
    while numeros < cantLetrasOcultar:
        largoPalabraSecreta = len(palabraSecreta)
        numero = randint(0,largoPalabraSecreta-1)
        if str(numero) not in secuencia:
            numeros = numeros +1
            secuencia = secuencia + str(numero)
            lisposiOcultar.append(numero)
    palabraTransformada = []
    for i in range(0,len(palabraSecreta)):
        if i in lisposiOcultar:
            palabraTransformada.append('_')
        else:
            palabraTransformada.append(palabraSecreta[i])
    palabra =''.join(palabraTransformada)
    return palabra

def revisar_letra(palabraSecreta, palabra, letra):
    listPalabraSecreta = list(palabraSecreta)
    palabra = list(palabra)
    if letra in listPalabraSecreta:
        i = palabraSecreta.find("-")
        palabra[i] = letra
    palabra = "".join(palabra)
    return palabra