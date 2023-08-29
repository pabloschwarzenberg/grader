# completa el código de la función
def suma_divisores(a):
  s=0
  p=0
  q=0
  for i in range(1,a):
    if a%i==0:
      s=s+i
      p=p+1
    if p==1:
      q=True
    else:
      q=False
   
         
        
  return s,q
           