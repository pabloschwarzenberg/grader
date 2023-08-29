import string

def estadisticas_frase(s):
    # Contar el número de palabras
    palabras = s.split()
    num_palabras = len(palabras)

    # Contar el número total de caracteres
    num_caracteres = len(s)

    # Calcular el largo promedio de las palabras
    suma_largos = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = suma_largos / num_palabras

    # Contar el número de espacios
    num_espacios = s.count(' ')

    # Contar el número de caracteres de puntuación
    caracteres_puntuacion = set(string.punctuation)
    num_puntuacion = sum(1 for caracter in s if caracter in caracteres_puntuacion)

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    poema = "El hombre imaginario\nvive en una mansión imaginaria\nrodeada de árboles imaginarios\na la orilla de un río imaginario\n\nDe los muros que son imaginarios\npenden antiguos cuadros imaginarios\nirreparables grietas imaginarias\nque representan hechos imaginarios\nocurridos en mundos imaginarios\nen lugares y tiempos imaginarios\n\nTodas las tardes tardes imaginarias\nsube las escaleras imaginarias\ny se asoma al balcón imaginario\na mirar el paisaje imaginario\nque consiste en un valle imaginario\ncircundado de cerros imaginarios..."

    resultado = estadisticas_frase(poema)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])

