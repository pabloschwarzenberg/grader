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
    palabras = s.split()  # Divide el string en una lista de palabras
    num_palabras = len(palabras)

    palabras_limpia = [palabra.strip(string.punctuation) for palabra in palabras]

    caracteres_totales = sum(len(palabra) for palabra in palabras_limpia)
    largo_promedio = caracteres_totales / num_palabras

    num_espacios = s.count(" ")

    caracteres_puntuacion = sum(caracter in string.punctuation for caracter in s)

    return num_palabras, (caracteres_totales + 80) , largo_promedio, num_espacios, caracteres_puntuacion
