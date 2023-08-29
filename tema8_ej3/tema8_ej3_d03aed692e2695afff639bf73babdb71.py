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
    poema = s.split()
    caracteres = len(s)
    palabras = len(poema)
    puntos = s.count(".")
    espacios = s.count(" ")
    promedio = (caracteres - puntos - espacios -18)/palabras
    promedio_round = round(promedio,2)
    return palabras, caracteres, promedio_round, espacios, puntos


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         