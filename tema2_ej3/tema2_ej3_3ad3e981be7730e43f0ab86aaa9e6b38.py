def numero_perfecto(a):
  sumador=0
  for i in range (1,a):
    if a%i==0:
        sumador+=i
  if sumador==a:
    return sumador,True
  else:
      return sumador,False
  
    return False


           