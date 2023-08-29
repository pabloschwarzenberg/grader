# completa el código de la función
def amigos(a,b):
  suma=0
  for i in range(2,a):
    if a%i==0:
      suma+=i
  suma+=1
  if suma==b:
    return True
  else: 
    return False
  for i in range(2,b):
    if b%i==0:
      suma+=i
  suma+=1
  if suma==a:
    return True  
  else:
    return False