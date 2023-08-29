# completa el código de la función
def suma_divisores(a):
  l = []
  for i in range(1,a-1):
    if a%i==0:
      l.append(i)
  s = sum(l)
  if s == 1:
    return s,True
  else:
    return s,False
           