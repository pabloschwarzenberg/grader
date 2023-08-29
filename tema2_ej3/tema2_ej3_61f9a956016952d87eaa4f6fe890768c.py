def numero_perfecto (a):
  f=1
  s=0
  while f < a:
    d = a%f
    if d == 0:
      s+=f
    f +=1
  return s==a