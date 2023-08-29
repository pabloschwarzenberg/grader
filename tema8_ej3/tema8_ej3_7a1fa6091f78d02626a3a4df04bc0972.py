import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra) for palabra in palabras)
    largo_promedio = num_caracteres / num_palabras
    num_espacios = s.count(' ')
    num_caracteres_puntuacion = sum(1 for char in s if char in string.punctuation)
    
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_caracteres_puntuacion

if __name__ == "__main__":
    s = "El hombre imaginario vive en una mansión imaginaria rodeada de árboles imaginarios a la orilla de un río imaginario. De los muros que son imaginarios penden antiguos cuadros imaginarios, irreparables grietas imaginarias que representan hechos imaginarios ocurridos en mundos imaginarios, en lugares y tiempos imaginarios. Todas las tardes tardes imaginarias sube las escaleras imaginarias y se asoma al balcón imaginario a mirar el paisaje imaginario que consiste en un valle imaginario circundado de cerros imaginarios..."
    resultado = estadisticas_frase(s)
    print(resultado)