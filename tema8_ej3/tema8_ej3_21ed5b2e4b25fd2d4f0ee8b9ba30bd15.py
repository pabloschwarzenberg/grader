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

  puntuacion = [",",";",".",":","¿","?","!","¡"]

  letra = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  pal = 0

  cac = 0

  pun = 0

  esp = 0

  ind = 0

  for i in frase:

    if i in letra and frase[ind+1] not in letra:

      pal += 1

    if i in letra:

      cac += 1

    if i in puntuacion:

      pun += 1

    if i not in letra and i not in puntuacion:

      esp += 1

    ind += 1

  frase2=list(frase)

  new2=len(frase2)

  esp2=0

  for e in frase2:

    if e==" ":

      esp2+=1

  prom_largo = cac/pal

  return pal,new2,prom_largo,esp2,pun



if __name__ == "__main__":

  print(estadisticas_frase(hombre_imaginario))