def estadisticas_frase(s):

    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = len(s)
    sum_largos = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = sum_largos / num_palabras
    num_espacios = s.count(' ')
    num_puntuacion = sum(1 for caracter in s if caracter in string.punctuation)
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion