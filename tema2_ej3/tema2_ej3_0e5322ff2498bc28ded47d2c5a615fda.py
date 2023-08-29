def numero_perfecto(a):
  x=0
  for i in range(1,a):
    division=a % (i) 
    if division == 0:
      x=x+(i)
  if x==a:
    return True
  else:
    return False