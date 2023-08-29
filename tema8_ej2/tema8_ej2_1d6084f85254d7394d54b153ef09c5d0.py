def buscarTodas(a,b):
  largo = len(a)
  i=0
  salida = ""
  while i<largo:
    if a.find(b,i,largo)>-1:
      salida = salida + " " + str(a.find(b,i,largo))
      if a.find(b,i,largo)==0:
        i=i+1
      else:
        i = 1 + a.find(b,i,largo)
       
    else:
      i=i+1
  return salida.strip()
           