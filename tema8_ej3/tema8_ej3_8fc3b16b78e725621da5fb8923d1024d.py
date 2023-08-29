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

  signos = [",",";",".",":","¿","?","!","¡"]

  abcdario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  palpico = 0

  cacasa = 0

  punpum = 0

  espanoil = 0

  indico = 0

  for i in frase:

    if i in abcdario and frase[indico+1] not in abcdario:

      palpico += 1

    if i in abcdario:

      cacasa += 1

    if i in signos:

      punpum += 1

    if i not in abcdario and i not in signos:

      espanoil += 1

    indico += 1

  frase2=list(frase)

  new2=len(frase2)

  esp2=0

  for e in frase2:

    if e==" ":

      esp2+=1

  prom_largo = cacasa/palpico

  return palpico,new2,prom_largo,esp2,punpum

  print(estadisticas_frase(hombre_imaginario))
         