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



def estadisticas_frase(f):

  f = f.lower()

  simbolo = ["¿","?",",",".",";",":","¡","!"]

  abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  x1 = 0

  x2 = 0

  x3 = 0

  x4 = 0

  x5 = 0

  for i in f:

    if(i in abc and f[x5+1] not in abc):

      x1 += 1

    if(i in abc):

      x2 += 1

    if(i in simbolo):

      x3 += 1

    if(i not in abc and i not in simbolo):

      x4 += 1

    x5 += 1

  y=list(f)

  y2=len(y)

  y3=0

  for e in y:

    if e==" ":

      y3+=1

  prom_largo = x2/x1

  return x1,y2,prom_largo,y3,x3
if __name__ == "_main_":

  print(estadisticas_f(hombre_imaginario))     