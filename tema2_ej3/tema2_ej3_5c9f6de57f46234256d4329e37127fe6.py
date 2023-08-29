def numero_perfecto(a):
  i=1
  suma=0
  if a==0:
    return False
  if a==1:
    return True
  while i<a:
    if a%i==0:
        suma+=i
    i+=1
  if suma==a:
    return True
  else:
    return False