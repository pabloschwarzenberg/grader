def buscarTodas(a,b):
  l = []
  f = ""
  for t in range(len(a)):
    l.append("-")
  x = -1
  j = []
  for i in a:
    if i == b:
      x = a.find(b,x + 1)
      print(x)
      j.append(x)
      f = f + "".join(str(x)) + " "
  g = f[:-1]
  
  return g
