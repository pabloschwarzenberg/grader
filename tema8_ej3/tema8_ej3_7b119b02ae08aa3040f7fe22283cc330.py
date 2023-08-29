import string

def estadisticas_frase(frase):
    # Remover caracteres de puntuación para contar palabras y caracteres
    frase_sin_puntuacion = frase.translate(str.maketrans("", "", string.punctuation))

    # Contar palabras
    palabras = frase_sin_puntuacion.split()
    num_palabras = len(palabras)

    # Calcular el número total de caracteres
    num_caracteres = sum(len(palabra) for palabra in palabras)

    # Calcular el largo promedio de las palabras
    if num_palabras > 0:
        largo_promedio = num_caracteres / num_palabras
    else:
        largo_promedio = 0

    # Contar espacios
    num_espacios = len(frase) - len(frase.replace(" ", ""))

    # Contar caracteres de puntuación
    num_puntuacion = len(frase) - len(frase_sin_puntuacion) - num_espacios

    # Retornar las estadísticas como un diccionario
    estadisticas = {
        "Número de palabras": num_palabras,
        "Número total de caracteres": num_caracteres,
        "Largo promedio de las palabras": largo_promedio,
        "Número de espacios": num_espacios,
        "Número de caracteres de puntuación": num_puntuacion
    }

    return estadisticas

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
    resultado = estadisticas_frase(hombre_imaginario)
    for clave, valor in resultado.items():
        print(clave + ":", valor)
