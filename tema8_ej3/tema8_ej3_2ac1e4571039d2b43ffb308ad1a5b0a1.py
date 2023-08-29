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
  signosdepuntuacion = [",",";",".",":","¿","?","!","¡"]
  abcedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
      "n","o","p","q","r","s","t","u","v","w","x","y","z",
      "á","í","é","ó","ú"]

  num_de_palabras = 0
  total_caracteres = 0
  numerodepuntuaciones = 0
  espacios = 0
  indice = 0

  for x in frase:
    if x in abcedario and frase[indice+1] not in abcedario:
      num_de_palabras += 1
    if x in abcedario:
      total_caracteres += 1
    if x in signosdepuntuacion:
      numerodepuntuaciones += 1
    if x not in abcedario and x not in signosdepuntuacion:
      espacios += 1
    indice += 1
  frasee=list(frase)
  total_caracteres2=len(frasee)
  (espacios2) =0
  for y in frasee:
    if y==" ":
      espacios2 +=1
  largo_promedio_palabras = total_caracteres/num_de_palabras
  return num_de_palabras,total_caracteres2,largo_promedio_palabras,espacios2,numerodepuntuaciones

if __name__ == "__main__":

  print(estadisticas_frase(hombre_imaginario))

         