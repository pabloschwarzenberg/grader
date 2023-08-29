hombreimaginario = """

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



def estadisticas_frase(n):

  n = n.lower()

  s = [",",";",".",":","¿","?","!","¡"]

  abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  uno1 = 0

  dos2 = 0

  tres3 = 0

  cuatro4 = 0

  cinco5 = 0

  for i in n:

    if i in abc and n[cinco5+1] not in abc:

      uno1 += 1

    if i in abc:

      dos2 += 1

    if i in s:

      tres3 += 1

    if i not in abc and i not in s:

      cuatro4 += 1

    cinco5 += 1

  f2=list(n)

  n2=len(f2)

  e2 = 0

  for e in f2:

    if e == " ":

      e2+=1

  prom_largo = dos2/uno1

  return uno1,n2,prom_largo,e2,tres3



if __name__ == "__main__":

  print(estadisticas_frase(hombreimaginario))



from string import ascii_letters