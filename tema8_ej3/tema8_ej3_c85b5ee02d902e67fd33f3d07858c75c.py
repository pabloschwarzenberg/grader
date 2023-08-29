import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra) for palabra in palabras)
    largo_promedio = num_caracteres / num_palabras if num_palabras > 0 else 0
    num_espacios = s.count(" ")
    num_puntuacion = sum(caracter in string.punctuation for caracter in s)

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion


