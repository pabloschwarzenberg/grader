import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra) for palabra in palabras)
    largo_promedio = num_caracteres / num_palabras

    num_espacios = s.count(' ')
    num_puntuacion = sum(caracter in string.punctuation for caracter in s)

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    s = """
    El hombre imaginario
    vive en una mansión imaginaria
    rodeada de árboles imaginarios
    a la orilla de un río imaginario

    De los muros que son imaginarios
    penden antiguos cuadros imaginarios
    irreparables grietas imaginarias
    que representan hechos imaginarios
    ocurridos en mundos imaginarios
    en lugares y tiempos imaginarios

    Todas las tardes tardes imaginarias    