def estadisticas_frase(s):
    palabras = s.split()
    numero_palabras = len(palabras)

    caracteres_totales = sum(len(palabra) for palabra in palabras)

    largo_promedio = caracteres_totales / numero_palabras

    numero_espacios = s.count(" ")

    caracteres_puntuacion = sum(1 for caracter in s if not caracter.isalpha() and caracter != " ")

    return numero_palabras, caracteres_totales, largo_promedio, numero_espacios, caracteres_puntuacion


if __name__ == "__main__":
    poema = """
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
    circundado de cerros imaginarios...
    """

    palabras, caracteres, promedio, espacios, puntuacion = estadisticas_frase(poema)
    print("Número de palabras:", palabras)
    print("Número total de caracteres:", caracteres)
    print("Largo promedio de las palabras:", promedio)
    print("Número de espacios:", espacios)
    print("Número de caracteres de puntuación:", puntuacion)
