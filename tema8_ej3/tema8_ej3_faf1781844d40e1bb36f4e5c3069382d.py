import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)

    caracteres_totales = len(s)
    caracteres_puntuacion = sum(caracter in string.punctuation for caracter in s)

    palabras_sin_puntuacion = [palabra.strip(string.punctuation) for palabra in palabras]
    caracteres_palabras = sum(len(palabra) for palabra in palabras_sin_puntuacion)

    num_espacios = s.count(" ")

    largo_promedio_palabras = caracteres_palabras / num_palabras

    return num_palabras, caracteres_totales, largo_promedio_palabras, num_espacios, caracteres_puntuacion

if __name__ == "__main__":
    texto = """El hombre imaginario
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

    resultado = estadisticas_frase(texto)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
