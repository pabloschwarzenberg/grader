def amigos(a, b):
  i=1
  l=0
  while i<a :
    if a%i==0 :
        l=l+i
    i=i+1
  j=1
  r=0
  while j<b :
    if b%j==0 :
        r=r+j
    j=j+1
  if l==b and r==a:
      return True
  else:
      return False
