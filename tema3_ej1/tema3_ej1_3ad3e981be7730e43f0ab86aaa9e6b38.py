def suma_divisores(a):
  sumador=0
  for i in range (1,a):
    if a%i==0:
        sumador+=i
  if sumador==1:
    return sumador,True
  else:
      return sumador,False
  

      
   

           