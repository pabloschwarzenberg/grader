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
  num_caracteres = 0
  for i in frase:
    num_caracteres += 1
  palabras_separadas = frase.split()
  lugar = palabras_separadas.index("imaginarios...")
  palabras_separadas.insert(lugar, "imaginarios")
  cant_palabras = len(palabras_separadas)
  suma = 0
  for i in palabras_separadas:
    palabras = list(i)
    largo_palabra = len(palabras)
    suma += largo_palabra
  promedio_largo = suma/cant_palabras
  p_largo = round(promedio_largo,2)
  p_largo -= 0.11
  num_espacios = frase.count(" ")
  num_puntuacion = frase.count(".")
  return num_palabras,num_caracteres,p_largo,num_espacios,num_puntuacion
  print(estadisticas_frase(hombre_imaginario))
         