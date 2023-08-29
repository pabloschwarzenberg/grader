import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    
    caracteres_totales = sum(len(palabra) for palabra in palabras)
    
    caracteres_puntuacion = sum(1 for c in s if c in string.punctuation)
    
    num_espacios = s.count(" ")
    
    largo_promedio = caracteres_totales / num_palabras if num_palabras > 0 else 0
    
    return num_palabras, caracteres_totales, largo_promedio, num_espacios, caracteres_puntuacion

if __name__ == "__main__":
    texto = """El hombre imaginario
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
    
    resultado = estadisticas_frase(texto)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])
