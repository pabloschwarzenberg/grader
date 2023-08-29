def numero_perfecto(a):
  suma=0
  divisor=1
  if a==0:
    return False
  elif a==1:
    return True
  while divisor<a:
    if a%divisor==0:
      suma+=divisor
    divisor +=1
  if a==suma:
        return True
  else:
        return False
           