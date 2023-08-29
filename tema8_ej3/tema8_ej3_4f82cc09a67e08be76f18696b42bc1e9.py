import string
def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = len(s)
    num_caracteres_palabras = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = num_caracteres_palabras / num_palabras if num_palabras > 0 else 0
    num_espacios = s.count(' ')

    caracteres_puntuacion = set(string.punctuation)
    num_puntuacion = sum(caracter in caracteres_puntuacion for caracter in s)
    
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

poema = '''El hombre imaginario
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

resultado = estadisticas_frase(poema)
print("número de palabras:", resultado[0])
print("número total de caracteres:", resultado[1])
print("largo promedio de las palabras:", resultado[2])
print("número de espacios:", resultado[3])
print("número de caracteres de puntuación:", resultado[4])
         