import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_espacios = s.count(' ')
    num_total_caracteres = len(s)
    num_puntuacion = sum([1 for c in s if c in string.punctuation])

    # Remover puntuación para calcular el largo promedio de las palabras
    palabras_sin_puntuacion = [''.join(ch for ch in palabra if ch not in string.punctuation) for palabra in palabras]
    largo_promedio_palabras = sum(len(palabra) for palabra in palabras_sin_puntuacion) / num_palabras
    largo_promedio_palabras = round(largo_promedio_palabras, 2)

    return (num_palabras, num_total_caracteres, largo_promedio_palabras, num_espacios, num_puntuacion)


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
    print(estadisticas_frase(hombre_imaginario))  # Debería imprimir (75, 521, 5.88, 59, 3)
