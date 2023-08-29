import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(p) for p in palabras)
    num_espacios = s.count(' ')
    puntuacion = set(string.punctuation)
    num_puntuacion = sum(1 for c in s if c in puntuacion and c != ' ')
    palabras_limpia = [p.strip(string.punctuation) for p in palabras]
    num_caracteres_palabras = sum(len(p) for p in palabras_limpia)
    largo_promedio = num_caracteres_palabras / num_palabras
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    s = """
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
    resultado = estadisticas_frase(s)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])
