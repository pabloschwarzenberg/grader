def numero_perfecto(a):
  i=0
  for x in range(1,a):
    if a%x==0:
      i=x+i
  return (i==a)