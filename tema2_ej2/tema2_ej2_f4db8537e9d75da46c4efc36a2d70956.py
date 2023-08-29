# completa el código de la función
def amigos(a,b):
  diva=0
  divb=0
  i=1
  if a==b:
    return False
  while i<=a:
    if a%i==0:
      diva=diva+i
    i=i+1
  j=1
  while j<=b:
    if b%j==0:
      divb=divb+j
    j=j+1
  if diva==divb:
    return True
  else:
    return False
      