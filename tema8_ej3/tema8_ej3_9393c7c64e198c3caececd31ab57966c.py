def estadisticas_frase(s):
    # Número de palabras
    palabras = s.split()
    num_palabras = len(palabras)

    # Número total de caracteres
    num_caracteres = len(s.replace(" ", ""))

    # Largo promedio de las palabras
    largo_promedio = sum(len(palabra) for palabra in palabras) / num_palabras

    # Número de espacios
    num_espacios = s.count(" ")

    # Número de caracteres de puntuación
    caracteres_puntuacion = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    num_puntuacion = sum(caracter in caracteres_puntuacion for caracter in s)

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

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

    resultado = estadisticas_frase(poema)
    print(resultado)