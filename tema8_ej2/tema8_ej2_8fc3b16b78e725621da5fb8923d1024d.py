def buscarTodas (a,b):
  indicar= ""
  numeros = 0
  for h in a:
    Nstr = str(numeros)
    if h == b:
      if indicar == "":
        indicar += Nstr
      else:
        indicar += " "
        indicar += Nstr
    numeros +=1
  return indicar
           