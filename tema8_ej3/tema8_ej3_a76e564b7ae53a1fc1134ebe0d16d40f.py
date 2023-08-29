import string

def estadisticas_frase(s):
    # Número de palabras
    palabras = s.split()
    num_palabras = len(palabras)

    # Número total de caracteres
    num_caracteres = len(s)

    # Largo promedio de las palabras
    sum_longitud = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = sum_longitud / num_palabras

    # Número de espacios
    num_espacios = s.count(" ")

    # Número de caracteres de puntuación
    caracteres_puntuacion = set(string.punctuation)
    num_puntuacion = sum(caracter in caracteres_puntuacion for caracter in s)

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion



    resultado = estadisticas_frase(poema)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])