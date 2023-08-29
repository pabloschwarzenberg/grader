import string

def estadisticas_frase(s):
    # Elimina los signos de puntuación y los reemplaza por espacios
    s = s.translate(str.maketrans('', '', string.punctuation.replace("'", "")))
    # Divide la cadena en palabras
    palabras = s.split()
    # Calcula el número de palabras
    num_palabras = len(palabras)
    # Calcula el número total de caracteres
    num_caracteres = sum(len(palabra) for palabra in palabras)
    # Calcula el largo promedio de las palabras
    largo_promedio = num_caracteres / num_palabras
    # Calcula el número de espacios
    num_espacios = s.count(' ')
    # Calcula el número de caracteres de puntuación
    num_puntuacion = sum(1 for c in s if c in string.punctuation.replace("'", ""))
    
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
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

    print(estadisticas_frase(poema))


    








         