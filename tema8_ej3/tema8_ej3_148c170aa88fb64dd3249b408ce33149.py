def estadisticas_frase(linea):
  linea = linea.lower()
  palabra = 0
  tilde = 0
  punto = 0
  espacio = 0
  indicador = 0
  puntuacion = [",",";",".",":","¿","?","!","¡"]
  abcdario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
      "n","o","p","q","r","s","t","u","v","w","x","y","z",
      "á","í","é","ó","ú"]
  for i in linea:
    if i in abcdario and linea[indicador+1] not in abcdario:
      palabra += 1
    if i in abcdario:
      tilde += 1
    if i in puntuacion:
      punto += 1
    if i not in abcdario and i not in puntuacion:
      espacio += 1
    indicador += 1
  frase=list(linea)
  nueva=len(frase)
  espn=0
  for e in frase:
    if e==" ":
      espn+=1
  largo = tilde/palabra
  return palabra,nueva,largo,espn,punto
if __name__=="__main__":
  print(estadisticas_frase(hombre_imaginario))