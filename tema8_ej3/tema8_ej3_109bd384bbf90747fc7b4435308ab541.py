import string

def estadisticas_frase(frase):
    num_palabras = len(frase.split())
    num_caracteres = len(frase)
    num_espacios = frase.count(' ')
    
    caracteres_puntuacion = string.punctuation.replace(' ', '')
    num_puntuacion = sum(frase.count(c) for c in caracteres_puntuacion)
    
    palabras = frase.split()
    num_caracteres_palabras = sum(len(p.strip(string.punctuation)) for p in palabras)
    largo_promedio = num_caracteres_palabras / num_palabras if num_palabras > 0 else 0
    
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
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
    circundado de cerros imaginarios...
    """
    
    resultados = estadisticas_frase(hombre_imaginario)
    print("Número de palabras:", resultados[0])
    print("Número total de caracteres:", resultados[1])
    print("Largo promedio de las palabras:", resultados[2])
    print("Número de espacios:", resultados[3])
    print("Número de caracteres de puntuación:", resultados[4])