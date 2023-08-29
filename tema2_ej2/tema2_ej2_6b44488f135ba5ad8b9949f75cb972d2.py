# completa el código de la función
def amigos(a,b):
  k=1
  j=1
  div_a=0 
  div_b=0
  for i in range(a-1):
    if a%k==0:
      div_a=div_a+k
    k=k+1
  for i in range(b-1):
    if b%j==0:
      div_b=div_b+j
    j=j+1
  if div_a==b and div_b==a:
    return True
  else:
    return False