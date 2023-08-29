import string

def estadisticas_frase(s):
    # Remover caracteres de puntuación
    s_sin_puntuacion = s.translate(str.maketrans('', '', string.punctuation))

    # Dividir la frase en palabras
    palabras = s_sin_puntuacion.split()

    # Número de palabras
    num_palabras = len(palabras)

    # Número total de caracteres
    num_caracteres = sum(len(palabra) for palabra in palabras)

    # Largo promedio de las palabras
    largo_promedio = num_caracteres / num_palabras if num_palabras > 0 else 0

    # Número de espacios
    num_espacios = s.count(' ')

    # Número de caracteres de puntuación
    caracteres_puntuacion = len(s) - len(s_sin_puntuacion)

    return num_palabras, num_caracteres, largo_promedio, num_espacios, caracteres_puntuacion

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

    resultado = estadisticas_frase(s)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])
