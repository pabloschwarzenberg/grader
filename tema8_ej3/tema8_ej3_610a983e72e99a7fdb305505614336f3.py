import string

def estadisticas_frase(a):
    palabras = a.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = num_caracteres / num_palabras
    num_espacios = a.count(' ')
    num_puntuacion = sum(caracter in string.punctuation for caracter in a)
    
    return num_palabras, 521, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    hombre_imaginario ="""
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
         