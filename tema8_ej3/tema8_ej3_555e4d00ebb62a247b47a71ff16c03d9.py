import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    
    caracteres_totales = sum(len(palabra) for palabra in palabras)
    caracteres_puntuacion = sum(palabra.count(c) for palabra in palabras for c in string.punctuation)
    
    num_espacios = s.count(" ")
    
    largo_promedio = caracteres_totales / num_palabras if num_palabras > 0 else 0
    
    return num_palabras, caracteres_totales, largo_promedio, num_espacios, caracteres_puntuacion