def estadisticas_frase(frase):
  frase = frase.lower()
  punt = [",",";",".",":","¿","?","!","¡"]
  bca = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
      "n","o","p","q","r","s","t","u","v","w","x","y","z",
      "á","í","é","ó","ú"]
  pal = 0
  cac = 0
  pun = 0
  esp = 0
  ind = 0
  for i in frase:
    if i in bca and frase[ind+1] not in bca:
      pal += 1
    if i in bca:
      cac += 1
    if i in punt:
      pun += 1
    if i not in bca and i not in punt:
      esp += 1
    ind += 1
  frase2=list(frase)
  new2=len(frase2)
  esp2=0
  for e in frase2:
    if e==" ":
      esp2+=1
  prom_largo = cac/pal
  return pal,new2,prom_largo,esp2,pun

if __name__ == "__main__":
  print(estadisticas_frase(hombre_imaginario))

from string import ascii_letters
