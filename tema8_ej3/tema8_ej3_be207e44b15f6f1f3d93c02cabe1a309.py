import string

def estadisticas_frase(s):
    num_palabras = len(s.split())
    num_caracteres = len(s)
    num_espacios = s.count(" ")
    num_puntuacion = sum([1 for c in s if c in string.punctuation])
    palabras = [palabra.strip(string.punctuation) for palabra in s.split()]
    largo_promedio_palabras = sum([len(palabra) for palabra in palabras])/num_palabras
    return num_palabras, num_caracteres, largo_promedio_palabras, num_espacios, num_puntuacion

    s = '''El hombre imaginario
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
circundado de cerros imaginarios...'''
    print(estadisticas_frase(s))