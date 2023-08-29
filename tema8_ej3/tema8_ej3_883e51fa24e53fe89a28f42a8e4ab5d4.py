import string

def estadisticas_frase(s):
    # Número de palabras
    palabras = s.split()
    num_palabras = len(palabras)

    # Número total de caracteres
    num_caracteres = len(s)

    # Largo promedio de las palabras
    suma_largos = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)
    largo_promedio = suma_largos / num_palabras

    # Número de espacios
    num_espacios = s.count(' ')

    # Número de caracteres de puntuación
    caracteres_puntuacion = set(string.punctuation)
    num_puntuacion = sum(1 for char in s if char in caracteres_puntuacion)

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

# Ejemplo de uso
poema = '''El hombre imaginario
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
circundado de cerros imaginarios...'''

resultado = estadisticas_frase(poema)
print("Número de palabras:", resultado[0])
print("Número total de caracteres:", resultado[1])
print("Largo promedio de las palabras:", resultado[2])
print("Número de espacios:", resultado[3])
print("Número de caracteres de puntuación:", resultado[4])

         