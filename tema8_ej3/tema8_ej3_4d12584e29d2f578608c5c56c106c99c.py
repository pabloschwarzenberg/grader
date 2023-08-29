import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = len(s)
    num_espacios = s.count(" ")
    num_puntuacion = sum([1 for c in s if c in string.punctuation])
    caracteres_palabras = sum([len(palabra.strip(string.punctuation)) for palabra in palabras])
    largo_promedio_palabras = caracteres_palabras / num_palabras
    return num_palabras, num_caracteres, largo_promedio_palabras, num_espacios, num_puntuacion

if __name__ == "__main__":
    s = """El hombre imaginario
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
    num_palabras, num_caracteres, largo_promedio_palabras, num_espacios, num_puntuacion = estadisticas_frase(s)
    print("Número de palabras:", num_palabras)
    print("Número total de caracteres:", num_caracteres)
    print("Largo promedio de las palabras:", largo_promedio_palabras)
    print("Número de espacios:", num_espacios)
    print("Número de caracteres de puntuación:", num_puntuacion)