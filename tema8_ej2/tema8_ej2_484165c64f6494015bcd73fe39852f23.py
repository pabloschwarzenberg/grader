def buscarTodas(a,b):
  list = []
  for x in range(len(a)):
    if(a[x] == b):
      list.append(str(x))
    s = ""
    for x in list:
      if x != list[-1]:
        s = s + x + " "
      else:
        s = s + x
  return s
  

           