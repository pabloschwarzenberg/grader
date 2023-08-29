import string

def estadisticas_frase(s):
    # Eliminar los signos de puntuación
    sin_puntuacion = s.translate(str.maketrans('', '', string.punctuation))
    
    # Dividir la frase en palabras
    palabras = sin_puntuacion.split()
    
    # Número de palabras
    num_palabras = len(palabras)
    
    # Número total de caracteres
    num_caracteres = sum(len(palabra) for palabra in palabras)
    
    # Largo promedio de las palabras
    largo_promedio = num_caracteres / num_palabras if num_palabras > 0 else 0
    
    # Número de espacios
    num_espacios = s.count(' ')
    
    # Número de caracteres de puntuación
    caracteres_puntuacion = set(string.punctuation)
    num_puntuacion = sum(1 for c in s if c in caracteres_puntuacion)
    
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
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
    
    num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion = estadisticas_frase(s)
    
    print("Número de palabras:", num_palabras)
    print("Número total de caracteres:", num_caracteres)
    print("Largo promedio de las palabras:", largo_promedio)
    print("Número de espacios:", num_espacios)
    print("Número de caracteres de puntuación:", num_puntuacion)
