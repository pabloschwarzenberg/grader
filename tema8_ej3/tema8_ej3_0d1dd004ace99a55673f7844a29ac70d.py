import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)

    caracteres_totales = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)

    largo_promedio = caracteres_totales / num_palabras if num_palabras > 0 else 0

    num_espacios = s.count(' ')

    caracteres_puntuacion = sum(1 for char in s if char in string.punctuation and char != ' ')

    return num_palabras, caracteres_totales, round(largo_promedio, 2), num_espacios, caracteres_puntuacion

texto = '''El hombre imaginario
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
circundado de cerros imaginarios'''

resultado = estadisticas_frase(texto)
print(resultado)
