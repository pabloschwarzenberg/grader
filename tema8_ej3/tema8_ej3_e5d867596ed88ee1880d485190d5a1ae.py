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



def estadisticas_frase (frase):

  frase = frase.lower()

  signos = [",",";",".",":","¿","?","!","¡"]

  letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  a = 0

  b = 0

  c = 0

  d = 0

  e = 0

  for i in frase:

    if i in letras and frase [e+1] not in letras:

      a += 1

    if i in letras:

      b += 1

    if i in signos:

      c += 1

    if i not in letras and i not in signos:

      d += 1

    e += 1

  oracion2=list(frase)

  nuevo=len(oracion2)

  d_2=0

  for e in oracion2:

    if e==" ":

      d_2+=1

  largo = b / a

  return a, nuevo , largo , d_2 , c



#if name == "main":

print(estadisticas_frase (hombre_imaginario))



from string import ascii_letters
