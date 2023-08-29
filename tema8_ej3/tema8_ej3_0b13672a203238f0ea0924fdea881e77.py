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

  s_de_p = [",", ";", ".", ":", "¿", "?", "!", "¡"]

  l_i = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  A = 0

  C = 0

  B = 0

  E = 0

  K = 0

  for i in x:

    if i in l_i and x[K + 1] not in l_i:

      A += 1

    if i in l_i:

      C += 1

    if i in s_de_p:

      B += 1

    if i not in l_i and i not in s_de_p:

      E += 1

    K += 1

  x_dos=list(x)

  largo_dos=len(x_dos)

  espacio_dos=0

  for k in x_dos:

    if k==" ":

      espacio_dos+=1

  largo_del_promedio = C / A

  return A, largo_dos, largo_del_promedio, espacio_dos, B