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

  frase_minuscula = frase.lower()

  Sub_punt = [",",";",".",":","¿","?","!","¡"]

  Sub_abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  Sub_pal = 0

  Sub_cac = 0

  Sub_pun = 0

  Sub_esp = 0

  Sub_ind = 0

  for i in frase_minuscula:

    if i in Sub_abc and frase[Sub_ind+1] not in Sub_abc:

      Sub_pal += 1

    if i in Sub_abc:

      Sub_cac += 1

    if i in Sub_punt:

      Sub_pun += 1

    if i not in Sub_abc and i not in Sub_punt:

      Sub_esp += 1

    Sub_ind += 1

  frase2=list(frase_minuscula)

  new2=len(frase2)

  esp2=0

  for e in frase2:

    if e==" ":

      esp2+=1

  prom_largo = Sub_cac/Sub_pal

  return Sub_pal,new2,prom_largo,esp2,Sub_pun



if __name__ == "__main__":

  print(estadisticas_frase(hombre_imaginario))



from string import ascii_letters
