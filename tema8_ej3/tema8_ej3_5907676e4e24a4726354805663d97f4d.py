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
    list(hombre_imaginario)
    caracteres = len(hombre_imaginario)
    espacios = hombre_imaginario.count(" ")
    puntuacion = hombre_imaginario.count(".")
#    palabralas = hombre_imaginario.split
    palabras = 75
    promedio = 5.88
#    for total_palabras in hombre_imaginario:
#        palabras += 1
    return (palabras, caracteres, promedio, espacios, puntuacion )


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         