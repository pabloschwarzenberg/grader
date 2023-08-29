import string
def estadisticas_frase(s):
    palabras = s.split()
    num_palabras = len(palabras)
    num_caracteres = len(s)
    largo_promedio = sum(len(palabra.strip(string.punctuation)) for palabra in palabras) / num_palabras
    num_espacios = s.count(' ')
    caracteres_puntuacion = sum(1 for caracter in s if caracter in string.punctuation and caracter != ' ') 
    estadisticas = ((num_palabras, num_caracteres, largo_promedio, num_espacios, caracteres_puntuacion))
    return estadisticas

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
circundado de cerros imaginarios....'''

resultado = estadisticas_frase(poema)
print(resultado)