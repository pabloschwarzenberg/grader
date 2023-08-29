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

  puntua = [",",";",".",":","¿","?","!","¡"]

  letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  n1 = 0

  n2 = 0

  n3 = 0

  n4 = 0

  n5 = 0

  for m in frase:

    if m in letras and frase[n5+1] not in letras:

      n1 += 1

    if m in letras:

      n2 += 1

    if m in puntua:

      n3 += 1

    if m not in letras and m not in puntua:

      n4 += 1

    n5 += 1

  f_2=list(frase)

  nuevo=len(f_2)

  n4_2=0

  for n in f_2:

    if n == " ":

      n4_2+=1

  promedio = n2/n1

  return n1,nuevo,promedio,n4_2,n3

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
    
from string import ascii_letters    