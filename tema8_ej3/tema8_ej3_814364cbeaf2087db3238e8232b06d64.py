import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = len(s)
    largo_promedio = sum(len(palabra.strip(string.punctuation)) for palabra in palabras) / num_palabras
    num_espacios = s.count(" ")
    num_puntuacion = sum(1 for c in s if c in string.punctuation)
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

         