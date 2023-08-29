def numero_perfecto(x):
  count=1
  suma=0
  while count!=x:
    if x%count==0:
      suma=suma+count
    count+=1
  if suma==x:
    return True
  else:
    return False
