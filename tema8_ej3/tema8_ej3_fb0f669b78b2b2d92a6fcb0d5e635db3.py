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

  signos = [",", ";", ".", ":", "¿", "?", "!", "¡"]

  letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n","o","p","q","r","s","t","u","v","w","x","y","z", "á","í","é","ó","ú"]

  word = 0

  characters = 0

  punctuation = 0

  spaces = 0

  average = 0

  for i in x:

    if i in letras and x[average+ 1] not in letras:

      word += 1

    if i in letras:

      characters += 1

    if i in signos:

      punctuation += 1

    if i not in letras and i not in signos:

      spaces += 1

    average += 1

  x_dos=list(x)

  largo_dos=len(x_dos)

  espacio_dos=0

  for k in x_dos:

    if k==" ":

      espacio_dos+=1

  largo_promedio = characters / word 

  return word , largo_dos, largo_promedio, espacio_dos, punctuation