# completa el código de la función
def amigos(a,b):
  p=1
  q=1
  sa=0
  sb=0
  while (p<a) and (q<b):
    if (a%p==0):
      sa=sa+p
    p=p+1
    if (b%q==0):
      sb=sb+q
    q=q+1
    
  if (sa==b) or (sb==a):
    return True
  else:
    return False
           