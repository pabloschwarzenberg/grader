# completa el código de la función
def amigos(a,b):
  l_a=0
  l_b=0
  for i in range(1,a):
    if a%i==0:
      l_a+=i
  for k in range(1,b):
    if b%k==0:
      l_b+=k
  if l_a==b and l_b==a:
    return True
  else:
    return False
    
  

           