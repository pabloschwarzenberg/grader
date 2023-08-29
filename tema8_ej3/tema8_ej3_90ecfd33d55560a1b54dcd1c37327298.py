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

  pxytos = [",",";",".",":","¿","?","!","¡"]

  abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","é","í","ó","ú"]

  asd = 0

  byz = 0

  pxy = 0

  cyz = 0

  rzy = 0

  for i in frase:

    if i in abecedario and frase[rzy+1] not in abecedario:

      asd += 1

    if i in abecedario:

      byz += 1

    if i in pxytos:

      pxy += 1

    if i not in abecedario and i not in pxytos:

      cyz += 1

    rzy += 1

  frase2=list(frase)

  new2=len(frase2)

  cyz2=0

  for e in frase2:

    if e==" ":

      cyz2+=1

  prom_largo = byz/asd

  return asd,new2,prom_largo,cyz2,pxy



if __name__ == "__main__":

  print(estadisticas_frase(hombre_imaginario))



from string import ascii_letters