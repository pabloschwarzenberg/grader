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

def estadisticas_frase(frase):
    palabras = frase.split()
    num_palabras = len(palabras)
    num_caracteres = len(frase)
    num_espacios = frase.count(' ')
    num_puntuacion = sum([1 for c in frase if c in string.punctuation])
    
    len_palabras = [len(w.strip(string.punctuation)) for w in palabras]

    promedio_largo_palabras = sum(len_palabras) / num_palabras
    
    return num_palabras, num_caracteres, promedio_largo_palabras, num_espacios, num_puntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         