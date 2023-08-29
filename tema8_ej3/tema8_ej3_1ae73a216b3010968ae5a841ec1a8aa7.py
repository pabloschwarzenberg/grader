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



def estadisticas_poema(poema):

  teclas = [",",";",".",":","¿","?","!","¡"]

  abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]
  poema = poema.lower()

  tap = 0

  cac = 0

  pun = 0

  esp = 0

  ind = 0


  for i in poema:

    if i in abecedario and poema[ind+1] not in abecedario:

      tap += 1

    if i in abecedario:

      cac += 1

    if i in teclas:

      pun += 1

    if i not in abecedario and i not in teclas:

      esp += 1

      ind += 1
  teclas2=''
  poema2 = ''
  frase2=list(poema)

  nuevo2=len(poema2)

  esp2=0


  for a in poema2:

    if a==" ":

      esp2=esp2+1

  prom = cac/tap

  return tap,nuevo2,prom,esp2,pun



if name == "main":

  print(estadisticas_poema(hombre_imaginario))



from string import ascii_letters