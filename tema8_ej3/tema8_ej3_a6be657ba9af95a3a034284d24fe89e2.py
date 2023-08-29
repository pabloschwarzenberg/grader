import string

def estadisticas_frase(s):
    # Contar el número de palabras
    palabras = s.split()
    num_palabras = len(palabras)

    # Calcular el número total de caracteres
    num_caracteres = len(s)

    # Calcular el largo promedio de las palabras
    suma_largos = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = suma_largos / num_palabras if num_palabras > 0 else 0

    # Contar el número de espacios
    num_espacios = s.count(" ")

    # Contar el número de caracteres de puntuación
    caracteres_puntuacion = [char for char in s if char in string.punctuation]
    num_caracteres_puntuacion = len(caracteres_puntuacion)

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_caracteres_puntuacion
