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


def estadisticas_frase(letra):

  letra = letra.lower()

  pu = [",",";",".",":","¿","?","!","¡"]

  acb = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  va = 0

  ve = 0

  vi = 0

  vo = 0

  vu = 0

  for i in letra:

    if i in acb and letra[vu+1] not in acb:

      va += 1

    if i in acb:

      ve += 1

    if i in pu:

      vi += 1

    if i not in acb and i not in pu:

      vo += 1

    vu += 1

  letra2=list(letra)

  ne2=len(letra2)

  vo2=0

  for e in letra2:

    if e==" ":

      vo2+=1

  pro_lar = ve/va

  return va,ne2,pro_lar,vo2,vi



if __name__ == "__main__":

  print(estadisticas_frase(hombre_imaginario))        