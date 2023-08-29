def suma_divisores(a):
  numero = a
  i = 1
  ndivisores = 0
  sumadivisores = 0
  while i < numero:
    if(numero % i == 0):
      sumadivisores += i
      ndivisores += 1
    i += 1
  if(ndivisores == 1):
    return (sumadivisores,True)
  return (sumadivisores,False)