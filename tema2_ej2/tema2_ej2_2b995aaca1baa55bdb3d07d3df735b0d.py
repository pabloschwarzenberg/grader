# completa el código de la función
def amigos(a,b):
  adiv=[1]
  bdiv=[1]
  i=2
  while i<a:
    if a%i==0:
      adiv.extend([i])
      i=i+1
    else:
      i=i+1
  j=2
  while j<b:
    if b%j==0:
      bdiv.extend([j])
      j=j+1
    else:
      j=j+1
  if sum(adiv)==b and a==sum(bdiv):
    return True
  else:
    return False
           