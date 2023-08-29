def buscarTodas(a,b):
  e = ""
  i = 0
  for letra in a:
      if b == letra:
        e = e + str(i) + " "
      i = i + 1 
  return e[:-1]