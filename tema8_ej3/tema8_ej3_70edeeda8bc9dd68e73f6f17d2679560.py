import string

def estadisticas_frase(s):
    num_palabras = len(s.split())
    num_caracteres = len(s)
    largo_promedio_palabras = sum(len(palabra.strip(string.punctuation)) for palabra in s.split()) / num_palabras
    num_espacios = s.count(' ')
    num_puntuacion = sum(1 for c in s if c in string.punctuation)
    return num_palabras, num_caracteres, largo_promedio_palabras, num_espacios, num_puntuacion

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

    palabras, caracteres, promedio, espacios, puntuacion = estadisticas_frase(poema)
    print("Palabras: ", palabras)
    print("Caracteres: ", caracteres)
    print("Largo promedio de palabras: ", promedio)
    print("Espacios: ", espacios)
    print("Puntuación: ", puntuacion)