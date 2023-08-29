import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    
    caracteres_totales = sum(len(palabra) for palabra in palabras)
    caracteres_puntuacion = sum(caracter in string.punctuation for palabra in palabras for caracter in palabra)
    caracteres_letras = sum(caracter.isalpha() for palabra in palabras for caracter in palabra)
    largo_promedio = (caracteres_totales-caracteres_puntuacion) / num_palabras if num_palabras > 0 else 0
    num_espacios = s.count(" ")
    num_caracteres_puntuacion = caracteres_puntuacion
    num_caracteres = len(s)
    
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_caracteres_puntuacion
