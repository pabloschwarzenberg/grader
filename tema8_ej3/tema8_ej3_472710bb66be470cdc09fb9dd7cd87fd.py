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

  PUNTOS = [",",";",".",":","¿","?","!","¡"]

  ABECEDARIO = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  A = 0

  B = 0

  C = 0

  D = 0

  E = 0

  for i in frase:

    if i in ABECEDARIO and frase[E+1] not in ABECEDARIO:

      A += 1

    if i in ABECEDARIO:

      B += 1

    if i in PUNTOS:

      C += 1

    if i not in ABECEDARIO and i not in PUNTOS:

      D += 1

    E += 1

  L2=list(frase)

  N2=len(L2)

  D2=0

  for X in L2:

    if X==" ":

      D2+=1

  prom_largo = B/A

  return A,N2,prom_largo,D2,C


if __name__ == "__main__":

  print(estadisticas_frase(hombre_imaginario))


from string import ascii_letters
