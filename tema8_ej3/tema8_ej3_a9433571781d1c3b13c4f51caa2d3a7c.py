import string

def estadisticas_frase(s):
    palabras = s.split()
    numero_palabras = len(palabras)
    numero_caracteres = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = numero_caracteres / numero_palabras
    numero_espacios = s.count(' ')
    caracteres_puntuacion = sum(1 for char in s if char in string.punctuation)

    return numero_palabras, numero_caracteres, largo_promedio, numero_espacios, caracteres_puntuacion