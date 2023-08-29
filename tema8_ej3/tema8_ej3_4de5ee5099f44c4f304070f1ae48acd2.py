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

  cosas = ["¿","?",",",".",";",":","¡","!"]

  abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  pal = 0

  cac = 0

  pun = 0

  esp = 0

  ind = 0

  for i in f:

    if(i in abecedario and f[ind+1] not in abecedario):

      pal += 1

    if(i in abecedario):

      cac += 1

    if(i in cosas):

      pun += 1

    if(i not in abecedario and i not in cosas):

      esp += 1

    ind += 1

  f2=list(f)

  nw2=len(f2)

  esp2=0

  for e in f2:

    if e==" ":

      esp2+=1

  prom_largo = cac/pal

  return pal,nw2,prom_largo,esp2,pun
if __name__ == "__main__":

  print(estadisticas_f(hombre_imaginario))
         