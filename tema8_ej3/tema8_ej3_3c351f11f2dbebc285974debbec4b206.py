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

  punteo = [",",";",".",":","¿","?","!","¡"]

  abcdario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  palabra = 0

  calculo = 0

  puntos = 0

  espacios_entre_si = 0

  indice = 0

  for i in frase:

    if i in abcdario and frase[indice+1] not in abcdario:

      palabra += 1

    if i in abcdario:

      calculo += 1

    if i in punteo:

      puntos += 1

    if i not in abcdario and i not in punteo:

      espacios_entre_si += 1

    indice += 1

  frase2=list(frase)

  new2=len(frase2)

  espacio2=0

  for e in frase2:

    if e==" ":

      espacio2+=1

  prom_largo = calculo/palabra

  return palabra,new2,prom_largo,espacio2,puntos
from string import ascii_letters