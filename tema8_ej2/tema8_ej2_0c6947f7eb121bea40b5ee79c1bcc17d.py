def buscarTodas(a,b):
  A=""
  for i in range(len(a)):
    if(i==b):
      print(b,"se encuentra en la variable")
      A=a.find(b)
      return (print(A))
      print(buscarTodas("tres tristes tigres","t"))