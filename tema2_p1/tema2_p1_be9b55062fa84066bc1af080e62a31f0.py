def primos(a):
  a=int(input( ))
  divisores=[]
  divisor=1
  while divisor<=a:
    if a%divisor==0:
      divisores.append(divisor)
    divisor+=1
  if len(divisores)==2:
    return True
  else:
    return False