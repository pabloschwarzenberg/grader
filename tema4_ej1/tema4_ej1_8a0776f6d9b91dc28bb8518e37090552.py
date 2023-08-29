import random

palabras = 'celular arbol lapiz carro'.split()

def buscarPalabraAleat(listaPalabras):
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]

palabraSecreta = buscarPalabraAleat(palabras)
cantidadLetras = '_'

def ocultarletras(palabra,cantidadw):
    palabrasas = palabra.replace('a',cantidadw)

    return palabrasas

print(ocultarletras(palabraSecreta,cantidadLetras))