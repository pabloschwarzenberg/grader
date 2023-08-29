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
  caracteres = [",",";",".",":","¿","?","!","¡"]
  abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
      "n","o","p","q","r","s","t","u","v","w","x","y","z",
      "á","í","é","ó","ú"]

  palabras = 0
  c = 0
  puntos = 0
  espacios = 0
  solo = 0

  for i in frase:
    if i in abecedario and frase[solo+1] not in abecedario:
      palabras += 1
    if i in abecedario:
      c += 1
    if i in caracteres:
      puntos += 1
    if i not in abecedario and i not in caracteres:
      espacios += 1
    solo += 1

  frase2=list(frase)
  nuevo2=len(frase2)
  espacios2=0

  for x in frase2:
    if x==" ":
      espacios2+=1
  largo = c/palabras
  return palabras,nuevo2,largo,espacios2,puntos

if __name__ == "__main__":

  print(estadisticas_frase(hombre_imaginario))


