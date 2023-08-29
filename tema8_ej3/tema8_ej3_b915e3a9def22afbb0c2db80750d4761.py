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
  palabras = len(frase)
  espacios = 0
  puntuacion = 0
  j = " "
  for j in frase:
    if j == " ":
      espacios = espacios + 1
    if j == ".":
      puntuacion = puntuacion +1
  frase = frase.strip(".")
  termino = len(frase.split())
  l_prom = list(frase.split())
  sumatoria = 0
  suma = 0
  for i in range(termino):
    sumatoria = len(l_prom[i])
    i = i + 1
    suma = suma + sumatoria
  promedio = suma/termino
  return termino, palabras, promedio, espacios, puntuacion