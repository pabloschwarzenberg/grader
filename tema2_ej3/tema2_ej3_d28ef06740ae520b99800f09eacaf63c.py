def numero_perfecto(a):
  count=1
  suma=0
  while count!=a:
    if a%count==0:
      suma+=count
    count+=1
      
  if suma==a:
    return True
  else:
    return False

           