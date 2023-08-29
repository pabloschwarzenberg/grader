import string

def estadisticas_frase(s):
    palabras = s.split()
    numero_palabras = len(palabras)
    numero_caracteres = sum(len(palabra) for palabra in palabras)
    largo_promedio = numero_caracteres / numero_palabras
    numero_espacios = s.count(" ")
    caracteres_puntuacion = sum(1 for caracter in s if caracter in string.punctuation and caracter != " ")

    return numero_palabras, numero_caracteres, largo_promedio, numero_espacios, caracteres_puntuacion

def contador_caracteres(cadena):
    return len(cadena)
cadena = """ El hombre imaginario
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

if __name__ == "__main__":
    frase = ''' El hombre imaginario
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
    resultado = estadisticas_frase(frase)
    resultado2 = contador_caracteres(cadena)
    print("(",resultado[0],",",resultado2,",",resultado[2],",",resultado[3],",",resultado[4],")")