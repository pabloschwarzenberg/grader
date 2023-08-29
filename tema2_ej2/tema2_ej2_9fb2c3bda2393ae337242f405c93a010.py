# completa el código de la función
def amigos(a,b):
  a=int(a)
  b=int(b)
  i=1
  diva=[]
  while i<a:
      if a%i==0:
          diva.append(i)
      i=i+1
  j=1
  divb=[]
  while j<b:
      if b%j==0:
          divb.append(j)
      j=j+1
  sumdiva=0
  sumdivb=0
  for k in diva:
      sumdiva=k+sumdiva
  for r in divb:
      sumdivb=r+sumdivb
  if sumdiva==b and sumdivb==a:
      return True
  else:
      return False
 
           