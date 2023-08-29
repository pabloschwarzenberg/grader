import string

def estadisticas_frase(frase):
    palabras = frase.split()
    num_palabras = len(palabras)
    num_caracteres = sum(len(palabra) for palabra in palabras)
    largo_promedio = num_caracteres / num_palabras
    num_espacios = frase.count(" ")
    num_puntuacion = sum(caracter in string.punctuation for caracter in frase if caracter != " ")

    return num_palabras, num_caracteres, round(largo_promedio, 2), num_espacios, num_puntuacion

if __name__ == "__main__":
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
    circundado de cerros imaginarios...
    """

    resultado = estadisticas_frase(hombre_imaginario)
    print(resultado)

         