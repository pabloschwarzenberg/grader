def buscarTodas (a,b):
  indico= ""
  numbers = 0
  for h in a:
    Nstr = str(numbers)
    if h == b:
      if indico == "":
        indico += Nstr
      else:
        indico += " "
        indico += Nstr
    numbers +=1
  return indico
           