import string

def estadisticas_frase(frase):
    # Contar el número de palabras
    palabras = frase.split()
    num_palabras = len(palabras)

    # Contar el número total de caracteres
    num_caracteres = sum(len(palabra) for palabra in palabras)

    # Calcular el largo promedio de las palabras
    largo_promedio = num_caracteres / num_palabras

    # Contar el número de espacios
    num_espacios = frase.count(' ')

    # Contar el número de caracteres de puntuación
    caracteres_puntuacion = string.punctuation.replace(' ', '')
    num_puntuacion = sum(caracter in caracteres_puntuacion for caracter in frase)

    # Retornar los resultados
    return {
        'Número de palabras': num_palabras,
        'Número total de caracteres': num_caracteres,
        'Largo promedio de las palabras': largo_promedio,
        'Número de espacios': num_espacios,
        'Número de caracteres de puntuación': num_puntuacion
    }

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
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")
