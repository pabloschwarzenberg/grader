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

def estadisticas_frase(frase):
    palabras = frase.split()
    num_palabras = len(palabras)
    num_caracteres = sum(caracter in frase for caracter in frase)
    largo_promedio = (sum(len(palabra) for palabra in palabras) - sum(caracter in '.,:;?!¿¡' for caracter in frase)) / num_palabras
    num_espacios = frase.count(" ")
    num_puntuacion = sum(caracter in '.,:;?!¿¡' for caracter in frase)

    return num_palabras, num_caracteres, largo_promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))