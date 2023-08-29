import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = num_caracteres / num_palabras if num_palabras > 0 else 0
    num_espacios = s.count(" ")
    num_puntuacion = sum(caracter in string.punctuation for caracter in s)
    
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    poema = """El hombre imaginario
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

    num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion = estadisticas_frase(poema)
    
    print("Número de palabras:", num_palabras)
    print("Número total de caracteres:", num_caracteres)
    print("Largo promedio de las palabras:", largo_promedio)
    print("Número de espacios:", num_espacios)
    print("Número de caracteres de puntuación:", num_puntuacion)
