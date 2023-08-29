import string

def estadisticas_frase(frase):
   
    palabras = frase.split()
    num_palabras = len(palabras)


    caracteres = len(frase)

    largo_palabras = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = largo_palabras / num_palabras

    num_espacios = frase.count(' ')

 
    caracteres_puntuacion = sum(1 for caracter in frase if caracter in string.punctuation)

    return num_palabras, caracteres, largo_promedio, num_espacios, caracteres_puntuacion

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
    circundado de cerros imaginarios..."""

    stats = estadisticas_frase(hombre_imaginario)
    print("Número de palabras:", stats[0])
    print("Número total de caracteres:", stats[1])
    print("Largo promedio de las palabras:", stats[2])
    print("Número de espacios:", stats[3])
    print("Número de caracteres de puntuación:", stats[4])
