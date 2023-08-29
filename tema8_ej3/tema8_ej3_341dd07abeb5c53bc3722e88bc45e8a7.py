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
  signos = [",",";",".",":","¿","?","!","¡"]
  letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
      "n","o","p","q","r","s","t","u","v","w","x","y","z",
      "á","í","é","ó","ú"]
  palabra = 0
  c = 0
  puntos = 0
  sp = 0
  asd = 0

  for i in frase:
    if i in letras and frase[asd+1] not in letras:
      palabra += 1
    if i in letras:
      c += 1
    if i in signos:
      puntos += 1
    if i not in letras and i not in signos:
      sp += 1
    asd += 1
  frase2=list(frase)
  n2=len(frase2)
  l2=0
  for e in frase2:
    if e==" ":
      l2+=1
  promedio_largo = c/palabra
  return palabra,n2,promedio_largo,l2,puntos

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         