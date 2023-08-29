import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)

    # Calcular el número total de caracteres y el largo promedio de las palabras
    num_caracteres = 0
    for palabra in palabras:
        palabra_limpia = palabra.strip(string.punctuation)
        num_caracteres += len(palabra_limpia)
    largo_promedio = num_caracteres / num_palabras

    # Contar el número de espacios
    num_espacios = sum(1 for caracter in s if caracter == ' ')

    # Contar el número de caracteres de puntuación
    num_puntuacion = sum(1 for caracter in s if caracter in string.punctuation and caracter != ' ')

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    frase = "El hombre imaginario\nvive en una mansión imaginaria\nrodeada de árboles imaginarios\na la orilla de un río imaginario\n\nDe los muros que son imaginarios\npenden antiguos cuadros imaginarios\nirreparables grietas imaginarias\nque representan hechos imaginarios\nocurridos en mundos imaginarios\nen lugares y tiempos imaginarios\n\nTodas las tardes tardes imaginarias\nsube las escaleras imaginarias\ny se asoma al balcón imaginario\na mirar el paisaje imaginario\nque consiste en un valle imaginario\ncircundado de cerros imaginarios..."
    resultado = estadisticas_frase(frase)
    print("Número de palabras:", resultado[0])
    print("Número total de caracteres:", resultado[1])
    print("Largo promedio de las palabras:", resultado[2])
    print("Número de espacios:", resultado[3])
    print("Número de caracteres de puntuación:", resultado[4])
