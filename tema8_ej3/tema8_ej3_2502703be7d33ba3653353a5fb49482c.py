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

import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = num_caracteres / num_palabras if num_palabras > 0 else 0
    
    num_espacios = s.count(' ')
    caracteres_puntuacion = sum(1 for char in s if char in string.punctuation and char != ' ')
    
    return num_palabras, num_caracteres, largo_promedio, num_espacios, caracteres_puntuacion

if __name__ == "__main__":
    frase = "El hombre imaginario\nvive en una mansión imaginaria\nrodeada de árboles imaginarios\na la orilla de un río imaginario\n\nDe los muros que son imaginarios\npenden antiguos cuadros imaginarios\nirreparables grietas imaginarias\nque representan hechos imaginarios\nocurridos en mundos imaginarios\nen lugares y tiempos imaginarios\n\nTodas las tardes tardes imaginarias\nsube las escaleras imaginarias\ny se asoma al balcón imaginario\na mirar el paisaje imaginario\nque consiste en un valle imaginario\ncircundado de cerros imaginarios..."
    resultado = estadisticas_frase(frase)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])

