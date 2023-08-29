import string

def estadisticas_frase(s):
    # Número de palabras
    palabras = s.split()
    num_palabras = len(palabras)
    
    # Número total de caracteres
    num_caracteres = len(s)
    
    # Largo promedio de las palabras
    suma_largos = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = suma_largos / num_palabras if num_palabras > 0 else 0
    
    # Número de espacios
    num_espacios = s.count(' ')
    
    # Número de caracteres de puntuación
    caracteres_puntuacion = set(string.punctuation)
    num_puntuacion = sum(1 for char in s if char in caracteres_puntuacion)
    
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

    resultados = estadisticas_frase(poema)
    print("Número de palabras:", resultados[0])
    print("Número total de caracteres:", resultados[1])
    print("Largo promedio de las palabras:", resultados[2])
    print("Número de espacios:", resultados[3])
    print("Número de caracteres de puntuación:", resultados[4])
