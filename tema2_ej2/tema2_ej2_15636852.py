def amigos(a,b):
  n=1
  y=0
  while n!=a:
    if a%n==0:
      y+=n
    n+=1
  m=1
  s=0
  while m!=b:
    if b%m==0:
      s+=m
    m+=1
   
  return y==b and s==a
           