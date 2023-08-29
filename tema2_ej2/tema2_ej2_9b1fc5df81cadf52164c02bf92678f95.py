# completa el código de la función
def amigos(a,b):
  c = range(1,a)
  g = 0
  for n in c:
    e=a%n
    if e==0:
      g=g+n
  d=range(1,b)
  h=0
  for m in d:
    f=b%m
    if f==0:
      h=h+m
  if a==h and b==g:
    return True
  else:
    return False
           