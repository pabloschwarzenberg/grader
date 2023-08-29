# completa el código de la función
def amigos(a,b):
  s = 0
  for i in range(1,a):
    if a%i == 0:
      s=s+i
  
  t = 0    
  for i in range(1,b):
    if b%i == 0:
      t=t+i
      
  if s==b and t==a:
    return True
  else:
    return False
      