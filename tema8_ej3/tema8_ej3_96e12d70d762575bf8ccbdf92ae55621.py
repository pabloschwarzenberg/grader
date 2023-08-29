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
def estadisticas_frase(oracion):
  caracteres = len(oracion)
  num_espacios = 0
  num_punto = 0
  j = " "
  for j in oracion:
    if j == " ":
      num_espacios = num_espacios + 1
    if j == ".":
      num_punto = num_punto +1
  oracion = oracion.strip(".")
  palabras = len(oracion.split())
  l_prom = list(oracion.split())
  sumatoria = 0
  suma = 0
  for i in range(palabras):
    sumatoria = len(l_prom[i])
    i = i + 1
    suma = suma + sumatoria
  promedio = suma/palabras
  return palabras, caracteres, promedio, num_espacios, num_punto
