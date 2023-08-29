def estadisticas_frase(frase):
  frase = frase.lower()
  punt = [",",";",".",":","¿","?","!","¡"]
  abc = ["á","í","é","ó","ú","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  pa = 0
  ca = 0
  pu = 0
  es = 0
  ind = 0
  for i in frase:
    if i in abc and frase[ind+1] not in abc:
      pa += 1
    if i in abc:
      ca += 1
    if i in punt:
      pu += 1
    if i not in abc and i not in punt:
      es += 1
    ind += 1
  frase2=list(frase)
  new2=len(frase2)
  es2=0
  for e in frase2:
    if e==" ":
      es2+=1
  prom_largo = ca/pa
  return pa,new2,prom_largo,es2,pu