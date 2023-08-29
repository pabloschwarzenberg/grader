import string

def estadisticas_frase(s):
    # Contar el número de palabras
    palabras = s.split()
    num_palabras = len(palabras)

    # Contar el número total de caracteres
    num_caracteres = len(s)

    # Calcular el largo promedio de las palabras
    sum_largos = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = sum_largos / num_palabras

    # Contar el número de espacios
    num_espacios = s.count(' ')

    # Contar el número de caracteres de puntuación
    num_puntuacion = sum(1 for caracter in s if caracter in string.punctuation)

    # Retornar los resultados como una tupla
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

# Ejemplo de uso con el fragmento del Hombre Imaginario de Nicanor Parra
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

resultados = estadisticas_frase(poema)
print("Número de palabras:", resultados[0])
print("Número total de caracteres:", resultados[1])
print("Largo promedio de las palabras:", resultados[2])
print("Número de espacios:", resultados[3])
print("Número de caracteres de puntuación:", resultados[4])   