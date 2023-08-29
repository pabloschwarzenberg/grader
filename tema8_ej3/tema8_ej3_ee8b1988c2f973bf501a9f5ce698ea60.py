import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)

    caracteres_totales = sum(len(palabra) for palabra in palabras)
    caracteres_sin_especiales = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    caracteres_puntuacion = caracteres_totales - caracteres_sin_especiales

    num_espacios = s.count(" ")

    largo_promedio = caracteres_sin_especiales / num_palabras

    return num_palabras, caracteres_totales, largo_promedio, num_espacios, caracteres_puntuacion

# Ejemplo de uso
frase = "El hombre imaginario\nvive en una mansión imaginaria\nrodeada de árboles imaginarios\na la orilla de un río imaginario\n\nDe los muros que son imaginarios\npenden antiguos cuadros imaginarios\nirreparables grietas imaginarias\nque representan hechos imaginarios\nocurridos en mundos imaginarios\nen lugares y tiempos imaginarios\n\nTodas las tardes tardes imaginarias\nsube las escaleras imaginarias\ny se asoma al balcón imaginario\na mirar el paisaje imaginario\nque consiste en un valle imaginario\ncircundado de cerros imaginarios..."

resultado = estadisticas_frase(frase)

print("Número de palabras:", resultado[0])
print("Número total de caracteres:", resultado[1])
print("Largo promedio de las palabras:", resultado[2])
print("Número de espacios:", resultado[3])
print("Número de caracteres de puntuación:", resultado[4])

