hombre_imaginario ="""
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
circundado de cerros imaginarios"""
def estadisticas_frase(frasee):

  frasee = frasee.lower()

  punt = [",",";",".",":","¿","?","!","¡"]

  abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  pal = 0

  cac = 0

  pun = 0

  esp = 0

  ind = 0

  for i in frasee:

    if i in abc and frasee[ind+1] not in abc:

      pal += 1

    if i in abc:

      cac += 1

    if i in punt:

      pun += 1

    if i not in abc and i not in punt:

      esp += 1

    ind += 1