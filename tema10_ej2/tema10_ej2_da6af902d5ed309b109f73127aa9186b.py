def levenshtein(palabra1,palabra2):
  DictPalabraMax= {}
  DictPalabraMin= {}
  palabramax=""
  subpalabra=""
  posibledistancia=0
  prueba=""

  if len(palabra2)>len(palabra1):
    palabramax=palabra2
    subpalabra=palabra1
  else:
    palabramax=palabra1
    subpalabra=palabra2

  subpalabraprueba= subpalabra+("_"*(len(palabramax)-len(subpalabra)))

  for rango in range(len(palabramax)):
    if palabramax[rango] not in DictPalabraMax:
      DictPalabraMax[palabramax[rango]] = 1
    else:
      DictPalabraMax[palabramax[rango]] = DictPalabraMax[palabramax[rango]]+1
  
  for elem in DictPalabraMax:
    posibledistancia+=(DictPalabraMax[elem]-subpalabra.count(elem))
  
  if palabramax==subpalabra:
    return "0D"
  elif posibledistancia >1:
    return "+1"
  elif len(palabramax)==len(subpalabra):
    for repeticion in range(len(palabramax)):
      if palabramax[repeticion]==subpalabra[repeticion]:
        prueba+=palabramax[repeticion]
      else:
        prueba+="_"
    if prueba.count("_")==1:
      return "1S"
    else:
      return "+1"
  else:
    conteo=0
    for repeticion in range(len(palabramax)):
      if palabramax[repeticion]==subpalabraprueba[repeticion] and conteo==0:
        prueba+=palabramax[repeticion]
      elif palabramax[repeticion]==subpalabraprueba[repeticion-1] and conteo>0:
        prueba+=palabramax[repeticion]
      elif subpalabraprueba[repeticion]=="_":
        prueba+=""
      else:
        prueba+="X"
        conteo+=1
    if prueba.count("X")==1:
      return "IB"
    else:
      return "+1"


levenshtein("jarron","jaron")