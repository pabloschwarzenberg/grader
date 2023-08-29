def buscarTodas (a,b):
  IF = "" 
  numero = 0 
  for x in a: 
    NString = str(numero)
    if x == b: 
      if IF == "": 
        IF += NString
      else: 
        IF += " "
        IF += NString 
    numero += 1
  return IF