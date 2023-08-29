import string

def estadisticas_frase(s):
    # Eliminar los caracteres especiales que no se consideran como parte de las palabras
    caracteres_especiales = string.punctuation.replace("'", "")
    s = s.translate(str.maketrans("", "", caracteres_especiales))

    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra) for palabra in palabras)
    largo_promedio_palabras = num_caracteres / num_palabras
    num_espacios = s.count(" ")
    num_caracteres_puntuacion = len(s) - num_caracteres - num_espacios

    return num_palabras, num_caracteres, largo_promedio_palabras, num_espacios, num_caracteres_puntuacion

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

    resultado = estadisticas_frase(poema)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])
