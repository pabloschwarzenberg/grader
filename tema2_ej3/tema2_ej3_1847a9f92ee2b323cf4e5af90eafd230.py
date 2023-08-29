def numero_perfecto(a):
  j=0
  for i in range(1,a):
    if a%i==0:
      j=j+i
  if a==j:
    return True
  else:
    return False

           