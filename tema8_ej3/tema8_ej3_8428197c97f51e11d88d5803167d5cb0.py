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
    # Eliminamos los caracteres especiales
    s = s.translate(str.maketrans('', '', string.punctuation))
    
    # Separamos las palabras por espacios
    palabras = s.split()
    
    # Calculamos las estadísticas
    num_palabras = len(palabras)
    num_caracteres = len(s)
    largo_promedio = sum(len(p) for p in palabras) / num_palabras
    num_espacios = s.count(' ')
    num_puntuacion = sum(c not in string.ascii_letters and c not in string.whitespace for c in s)
    
    # Retornamos las estadísticas
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion
         