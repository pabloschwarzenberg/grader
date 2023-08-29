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

def estadisticas_frase(s):
    numero_palabras = 0

    total_caracteres = len(s)

    palabras = s.split()
    suma = 0
    for i in range(0,len(palabras)):
        palabra = ''.join(char for char in palabras[i] if char.isalnum())
        if(palabra):
            numero_palabras += 1
            suma += len(palabra)

    avg_largo_palabras = suma/numero_palabras

    numero_espacios = s.count(" ")

    caracteres_puntuacion = s.count(".")+s.count(",")+s.count(":")+s.count(";")
    
    return numero_palabras, total_caracteres, avg_largo_palabras, numero_espacios, caracteres_puntuacion



         