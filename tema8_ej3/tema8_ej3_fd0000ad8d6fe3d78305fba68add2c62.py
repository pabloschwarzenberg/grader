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

def estadisticas_frase(x):

  x = x.lower()

  signos_de_puntuacion = [",", ";", ".", ":", "¿", "?", "!", "¡"]

  letras_incluidas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  pa = 0

  c = 0

  pu = 0

  e = 0

  j = 0

  for i in x:

    if i in letras_incluidas and x[j + 1] not in letras_incluidas:

      pa += 1

    if i in letras_incluidas:

      c += 1

    if i in signos_de_puntuacion:

      pu += 1

    if i not in letras_incluidas and i not in signos_de_puntuacion:

      e += 1

    j += 1

  x_dos=list(x)

  largo_dos=len(x_dos)

  espacio_dos=0

  for k in x_dos:

    if k==" ":

      espacio_dos+=1

  largo_del_promedio = c / pa

  return pa, largo_dos, largo_del_promedio, espacio_dos, pu