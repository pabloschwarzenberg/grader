def ecuaciones(string):
  lista=[]
  listainicial=string.split(" ")

  x = int(listainicial[0])
  y = int(listainicial[1])
  n = int(listainicial[2])
  x2 = int(listainicial[3])
  y2 = int(listainicial[4])
  n2 = int(listainicial[5])
  print(listainicial)


  xa = x*(-x2)
  ya =  y*(-x2)
  na =  n*(-x2)

  x2a = x2*(x)
  y2a =  y2*(x)
  n2a =  n2*(x)

  variabley= ya+y2a
  enteros= na+n2a
  finaly = enteros/variabley

  finalyx= (n - y*(finaly))/x

  yf = "x="+str(finalyx)
  lista.append(yf)
  yf = "y="+str(finaly)
  lista.append(yf)
  print(lista)