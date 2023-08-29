import string

def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    
    caracteres = ''.join(c for c in s if c.isalpha() or c.isspace())
    num_caracteres = len(caracteres)
    
    largo_palabras = [len(palabra) for palabra in palabras]
    largo_promedio = sum(largo_palabras) / num_palabras
    
    num_espacios = s.count(' ')
    
    caracteres_puntuacion = ''.join(c for c in s if c in string.punctuation and c not in (' ', '...'))
    num_puntuacion = len(caracteres_puntuacion)
    
    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

# Fragmento del poema "El Hombre Imaginario" de Nicanor Parra
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

