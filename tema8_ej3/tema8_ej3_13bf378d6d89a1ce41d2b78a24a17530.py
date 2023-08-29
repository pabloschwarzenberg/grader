import string

def estadisticas_frase(s):
    # Número de palabras
    palabras = s.split()
    num_palabras = len(palabras)

    # Número total de caracteres
    caracteres_totales = len(s)

    # Largo promedio de las palabras
    suma_largos = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = suma_largos / num_palabras

    # Número de espacios
    num_espacios = s.count(' ')

    # Número de caracteres de puntuación
    caracteres_puntuacion = len([char for char in s if char in string.punctuation])

    # Retornar los resultados en un diccionario
    estadisticas = {
        'numero_palabras': num_palabras,
        'total_caracteres': caracteres_totales,
        'largo_promedio': largo_promedio,
        'numero_espacios': num_espacios,
        'caracteres_puntuacion': caracteres_puntuacion
    }
    return estadisticas

# Ejemplo de uso con el fragmento del poema
poema = '''El hombre imaginario
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
circundado de cerros imaginarios...'''

resultados = estadisticas_frase(poema)
print(resultados)