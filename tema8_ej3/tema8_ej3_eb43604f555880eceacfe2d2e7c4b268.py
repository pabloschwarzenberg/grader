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
  s=hombre_imaginario.split()
  numero_palabras=len(s)
  numero_=hombre_imaginario.count(" ")
  numero_puntos=hombre_imaginario.count(".")
  numero_caracteres=len(hombre_imaginario)
  promedio=(numero_caracteres-numero_puntos-numero_-18)/numero_palabras
  return numero_palabras,numero_caracteres,promedio,numero_,numero_puntos

    