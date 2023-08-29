def suma_divisores(x):
  #PROCESAMIENTO
  suma = 0
  DAB = x
  #CICLO DAB!
  while DAB > 1:
    DAB = DAB - 1
    if (x% DAB) == 0:
        suma += DAB
  #RETURN DE LA SUMA
  if suma == 1:
      return suma,True
  if suma != 1:
      return suma,False
           