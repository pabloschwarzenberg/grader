import string

def estadisticas_frase(frase):
    # Número de palabras
    palabras = frase.split()
    num_palabras = len(palabras)

    # Número total de caracteres
    caracteres_totales = len(frase)

    # Largo promedio de las palabras
    largo_promedio = sum(len(palabra.strip(string.punctuation)) for palabra in palabras) / num_palabras

    # Número de espacios
    num_espacios = frase.count(' ')

    # Número de caracteres de puntuación (que no sean letras o espacios)
    caracteres_puntuacion = sum(caracter in string.punctuation for caracter in frase)

    return num_palabras, caracteres_totales, largo_promedio, num_espacios, caracteres_puntuacion

hombre_imaginario = """
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
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
