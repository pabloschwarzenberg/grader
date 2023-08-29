hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

def estadisticas_frase(frase):
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

import string

def estadisticas_frase(s):
    # Contar el número de palabras
    palabras = s.split()
    num_palabras = len(palabras)

    # Calcular el número total de caracteres
    num_caracteres = len(s)

    # Calcular el largo promedio de las palabras
    suma_largos = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = suma_largos / num_palabras if num_palabras > 0 else 0

    # Contar el número de espacios
    num_espacios = s.count(" ")

    # Contar el número de caracteres de puntuación
    caracteres_puntuacion = [char for char in s if char in string.punctuation]
    num_caracteres_puntuacion = len(caracteres_puntuacion)

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_caracteres_puntuacion         