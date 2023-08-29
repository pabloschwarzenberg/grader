def buscarTodas(a,b):
  final=""
  comienzo=0
  conteo= a.count(b)
  for repeticiones in range (conteo):
    variable= a[comienzo:].find(b)
    comienzo += variable+1
    final +=str(comienzo-1)+" "
  finales=final[0:len(final)-1]
  return finales