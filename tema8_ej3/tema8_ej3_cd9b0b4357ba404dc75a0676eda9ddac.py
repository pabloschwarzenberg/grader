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

  frase = frase.lower()

  simbolos = [",",";",".",":","¿","?","!","¡"]

  letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  x = 0
  y = 0
  z = 0
  y2 = 0
  x2 = 0

  for i in frase:

    if i in letras and frase[x2+1] not in letras:

      x += 1

    if i in letras:

      y += 1

    if i in simbolos:

      z += 1

    if i not in letras and i not in simbolos:

      y2 += 1

    x2 += 1

  Frase_2=list(frase)

  new2=len(Frase_2)

  esp2=0

  for e in Frase_2:

    if e==" ":

      esp2+=1

  prom_largo = y/x

  return x,new2,prom_largo,esp2,z