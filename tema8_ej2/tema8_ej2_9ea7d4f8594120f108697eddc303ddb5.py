def buscarTodas(a,b):
  apariciones = ''
  for i in range(len(a)):
    if b == a[i]:
      apariciones = apariciones + ' ' + str(i)
  return apariciones
