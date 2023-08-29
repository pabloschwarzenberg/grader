import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = num_caracteres / num_palabras
    num_espacios = s.count(" ")
    caracteres_puntuacion = sum(1 for char in s if char in string.punctuation)

    return num_palabras, num_caracteres, round(largo_promedio, 2), num_espacios, caracteres_puntuacion

if __name__ == "__main__":
    frase = """
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
    circundado de cerros imaginarios...
    """
    
    resultados = estadisticas_frase(frase)
    print("Estadísticas:")
    print("Número de palabras:", resultados[0])
    print("Número total de caracteres:", resultados[1])
    print("Largo promedio de las palabras:", resultados[2])
    print("Número de espacios:", resultados[3])
    print("Número de caracteres de puntuación:", resultados[4])
