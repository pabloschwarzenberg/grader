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

def estadisticas_frase(palabra):
  palabra = palabra.lower()
  signos = [",", ";", ".", ":", "¿", "?", "!", "¡"]
  letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
         "á", "í", "é", "ó", "ú"]
  uno = 0
  dos = 0
  tres = 0
  cuatro = 0
  cinco = 0

  for i in palabra:
    if i in letras and palabra[cinco + 1] not in letras:
      uno += 1
    if i in letras:
      dos += 1
    if i in signos:
      tres += 1
    if i not in letras and i not in signos:
      cuatro += 1
    cinco += 1

  frase2 = list(palabra)
  new2 = len(frase2)
  esp2 = 0

  for e in frase2:
    if e==" ":
      esp2+=1
  prom_largo = dos/uno
  return uno,new2,prom_largo,esp2,tres

if __name__ == "_main_":
  print(estadisticas_frase(hombre_imaginario))
         