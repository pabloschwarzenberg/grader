import string

def estadisticas_frase(s):
    # Eliminar los caracteres especiales y convertir a minúsculas
    s = ''.join(c for c in s if c.isalpha() or c.isspace())
    s = s.lower()

    # Dividir la frase en palabras
    palabras = s.split()

    # Número de palabras
    num_palabras = len(palabras)

    # Número total de caracteres
    num_caracteres = sum(len(palabra) for palabra in palabras)

    # Largo promedio de las palabras
    largo_promedio = num_caracteres / num_palabras if num_palabras > 0 else 0

    # Número de espacios
    num_espacios = s.count(' ')

    # Número de caracteres de puntuación
    num_puntuacion = sum(1 for c in s if c in string.punctuation and c != '...')

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

# Prueba del programa
if __name__ == "__main__":
    poema = """El hombre imaginario
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

    num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion = estadisticas_frase(poema)

    print("Número de palabras:", num_palabras)
    print("Número total de caracteres:", num_caracteres)
    print("Largo promedio de las palabras:", largo_promedio)
    print("Número de espacios:", num_espacios)
    print("Número de caracteres de puntuación:", num_puntuacion)