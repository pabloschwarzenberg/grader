def buscarTodas(a,b):
  A=""
  for n in range(len(a)):
    if b in a:
      A=a.find(b)
      return (print(A))
  print(buscarTodas("tres tristes tigres","t"))