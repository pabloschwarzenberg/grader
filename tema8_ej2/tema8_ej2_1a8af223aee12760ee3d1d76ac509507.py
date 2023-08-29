def buscarTodas (a,b):
  posciciones = ""
  numero = 0
  for i in a:
    if i == b:
      if posciciones == " ":
       numerostr = str(numero)
       posciciones += numerostr
      else:
       posciciones += " "
       numerostr = str(numero)
       posciciones += numerostr
       numero += 1
    else:
      numero += 1
  
  return posciciones