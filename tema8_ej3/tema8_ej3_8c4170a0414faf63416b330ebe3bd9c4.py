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

#ENTRADA

def estadisticas_frase(f):

  f = f.lower()

  punt = [",",";",".",":","¿","?","!","¡"]
  
  abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]
      
#PROCESAMIENTO

  r = 0

  s = 0

  y = 0

  o = 0

  p = 0

  for i in f:

    if i in abc and f[o+1] not in abc:

      p += 1

    if i in punt:

      s += 1
      
    if i in abc:

      y += 1

    if i not in abc and i not in punt:

      r += 1

    o += 1

  palabraf=list(f)

  a=len(palabraf)

  u=0

  for e in palabraf:

    if e==" ":

      u += 1

  frase_variable = y/p

  return p,a,frase_variable,u,s
  
#SALIDA

if __name__ == "__main__":

  print(estadisticas_frase(promedio))



from string import ascii_letters