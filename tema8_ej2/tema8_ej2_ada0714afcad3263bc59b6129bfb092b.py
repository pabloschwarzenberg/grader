def buscarTodas (a,b):
  funcionn = "" 
  numero = 0 
  for x in a: 
    numeroString = str(numero)
    if x == b: 
      if funcionn == "": 
        funcionn += numeroString 
      else: 
        funcionn += " "
        funcionn += numeroString 
    numero +=1
  return funcionn