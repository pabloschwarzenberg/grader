import string

def estadisticas_frase(s):
    # Contar número de palabras
    num_palabras = len(s.split())

    # Contar número total de caracteres
    num_caracteres = len(s)

    # Calcular longitud promedio de palabras
    palabras = s.translate(str.maketrans('', '', string.punctuation)).split()
    promedio_longitud_palabra = sum(len(palabra) for palabra in palabras) / len(palabras)

    # Contar número de espacios
    num_espacios = s.count(' ')

    # Contar número de caracteres de puntuación
    caracteres_puntuacion = string.punctuation.replace("'", "") # el apostrofe no se considera puntuación
    num_caracteres_puntuacion = sum(s.count(caracter) for caracter in caracteres_puntuacion)

    return (num_palabras, num_caracteres, promedio_longitud_palabra, num_espacios, num_caracteres_puntuacion)
