import random
def ocultar_letras(palabra,cantidad):
    for letra in range(cantidad+1):
        posicion = random.randint(0,len(palabra)-1)
        print(posicion)
        print(palabra[posicion])
        palabra = palabra.replace(palabra[posicion],'_')

    return palabra