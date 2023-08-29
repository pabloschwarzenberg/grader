import string

def estadisticas_frase(frase):
    # Eliminar los caracteres de puntuación y convertir a minúsculas
    frase_limpia = frase.translate(str.maketrans("", "", string.punctuation)).lower()

    # Dividir la frase en palabras
    palabras = frase_limpia.split()

    # Calcular el número de palabras
    num_palabras = len(palabras)

    # Calcular el número total de caracteres
    num_caracteres = sum(len(palabra) for palabra in palabras)

    # Calcular el largo promedio de las palabras
    largo_promedio = num_caracteres / num_palabras if num_palabras > 0 else 0

    # Calcular el número de espacios
    num_espacios = frase.count(" ")

    # Calcular el número de caracteres de puntuación
    num_puntuacion = sum(caracter in string.punctuation for caracter in frase_limpia)

    # Retornar los resultados como una tupla
    estadisticas = (num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion)

    return estadisticas

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

    resultado = estadisticas_frase(hombre_imaginario)
    print(resultado)
