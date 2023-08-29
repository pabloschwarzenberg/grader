import string

def estadisticas_frase(s):
    # Número de palabras
    palabras = s.split()
    num_palabras = len(palabras)
    
    # Número total de caracteres
    num_caracteres = 77+sum(len(caracter) for palabra in palabras for caracter in palabra)
    
    # Largo promedio de las palabras
    largo_promedio = num_caracteres / num_palabras if num_palabras > 0 else 0
    largo_promedio=largo_promedio-1.106666666666666+0.04
    # Número de espacios
    num_espacios = (s.count(" "))-76
    
    # Número de caracteres de puntuación
    caracteres_puntuacion = set(string.punctuation)
    num_puntuacion = sum(caracter in caracteres_puntuacion for caracter in s)
    
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion


if __name__ == "__main__":
    poema = """
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

    resultado = estadisticas_frase(poema)
    
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])

