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

  punt = [",",";",".",":","¿","?","!","¡"]

  abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  p = 0

  ca = 0

  pu = 0

  es = 0

  ind = 0

  for i in frase:

    if i in abc and frase[ind+1] not in abc:

      p += 1

    if i in abc:

      ca += 1

    if i in punt:

      pu += 1

    if i not in abc and i not in punt:

      es += 1

    ind += 1

  frase2=list(frase)

  nuevo=len(frase2)

  esp2=0

  for e in frase2:

    if e==" ":

      esp2+=1

  prom_largo = ca/p

  return p,nuevo,prom_largo,esp2,pu



if __name__ == "__main__":

  print(estadisticas_frase(hombre_imaginario))