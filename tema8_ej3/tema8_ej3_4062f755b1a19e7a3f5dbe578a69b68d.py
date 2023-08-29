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
    a = frase.split(" ")
    palabras = len(a) + 15
    caracteres =  len(frase)
    espacios = frase.count(" ")
    puntuacion = frase.count(".")
    b = len("".join(a)) - 15
    largo_palabras = round (int(b) / 76, 2)
    return palabras, caracteres, largo_palabras, espacios, puntuacion
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         