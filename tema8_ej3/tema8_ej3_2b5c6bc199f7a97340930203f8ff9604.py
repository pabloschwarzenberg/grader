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

  letritas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  palabras = 0

  caracteres = 0

  puntuaciones = 0

  espaciosss = 0

  j = 0

  for i in x:

    if i in letritas and x[j + 1] not in letritas:

      palabras += 1

    if i in letritas:

      caracteres += 1

    if i in signos_de_puntuacion:

      puntuaciones += 1

    if i not in letritas and i not in signos_de_puntuacion:

      espaciosss += 1

    j += 1

  x_dos=list(x)

  largo_dos=len(x_dos)

  espacio_dos=0

  for k in x_dos:

    if k==" ":

      espacio_dos+=1

  promedio_largo = caracteres / palabras

  return palabras, largo_dos, promedio_largo, espacio_dos, puntuaciones



if __name__ == "__main__":

  print(estadisticas_frase(hombre_imaginario))

         