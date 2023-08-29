# completa el código de la función
def suma_divisores(a):
  s = 0
  for i in range(1, a-1):
    if a%i==0:
      s = s+i
        
  if s==1:
    return s,True
  else:
    return s,False
          