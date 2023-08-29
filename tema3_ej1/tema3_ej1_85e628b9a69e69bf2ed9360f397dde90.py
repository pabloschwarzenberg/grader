# completa el código de la función
def suma_divisores(a):
  n=2
  s=1
  p=0
  while n<a:
     k=a%n
     if k==0:
        s=s+n
        p=1
     n+=1
  if p==1:
     h=False
  else:
     h=True
  if a==1:
     s=0
     h=False
  return s, h