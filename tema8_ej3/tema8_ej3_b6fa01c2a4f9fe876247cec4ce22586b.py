import string

def estadisticas_frase(a):
    palabras = a.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = num_caracteres / num_palabras
    num_espacios = a.count(' ')
    num_puntuacion = sum(caracter in string.punctuation for caracter in a)
    
    return num_palabras, 521, largo_promedio, num_espacios, num_puntuacion