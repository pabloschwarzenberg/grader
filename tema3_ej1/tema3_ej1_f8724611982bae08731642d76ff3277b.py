# completa el código de la función

def suma_divisores(n):
  divisor=2
  a=1
  while divisor<n:
      if n%divisor==0:
          a=a+divisor
      divisor+=1
    
  if a!=1:
      return a,False
  elif n==1:
      return 0,False
  else:
      return a,True
    



           