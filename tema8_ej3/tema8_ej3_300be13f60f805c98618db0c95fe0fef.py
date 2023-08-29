import string

def estadisticas_frase(s):
    # Número de palabras
    palabras = s.split()
    num_palabras = len(palabras)

    # Número total de caracteres
    num_caracteres = len(s)

    # Largo promedio de las palabras
    caracteres_palabras = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = caracteres_palabras / num_palabras

    # Número de espacios
    num_espacios = s.count(' ')

    # Número de caracteres de puntuación
    caracteres_puntuacion = sum(1 for c in s if c in string.punctuation)

    return num_palabras, num_caracteres, largo_promedio, num_espacios, caracteres_puntuacion

if __name__ == "__main__":
    frase = "El hombre imaginario\nvive en una mansión imaginaria\nrodeada de árboles imaginarios\na la orilla de un río imaginario\n\nDe los muros que son imaginarios\npenden antiguos cuadros imaginarios\nirreparables grietas imaginarias\nque representan hechos imaginarios\nocurridos en mundos imaginarios\nen lugares y tiempos imaginarios\n\nTodas las tardes tardes imaginarias\nsube las escaleras imaginarias\ny se asoma al balcón imaginario\na mirar el paisaje imaginario\nque consiste en un valle imaginario\ncircundado de cerros imaginarios..."
    
    resultado = estadisticas_frase(frase)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])
