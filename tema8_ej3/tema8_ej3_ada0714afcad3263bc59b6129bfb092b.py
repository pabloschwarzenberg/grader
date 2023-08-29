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

  abcde = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  a = 0

  b = 0

  c = 0

  d = 0

  e = 0

  for i in frase:

    if i in abcde and frase[e+1] not in abcde:

        a += 1

    if i in abcde:

      b += 1

    if i in punt:

      c += 1

    if i not in abcde and i not in punt:

      d += 1

    e += 1

  frase2=list(frase)

  new2=len(frase2)

  esp2=0

  for e in frase2:

    if e==" ":

      esp2+=1

  prom_largo = b/a

  return    a,new2,prom_largo,esp2,c




         