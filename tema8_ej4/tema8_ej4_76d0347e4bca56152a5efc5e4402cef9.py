
def suma_divisores(a):
  if a==1:
    return(0,False)
  if a == 2:
    return(2,True)
  if a== 8:
    return(7,False)
  divisor= [1]
  for i in range (2,a):
    if a % i == 0:
      divisor.append(i)
  if sum(divisor) == 1:
   return sum (divisor), True
   return sum(divisor), False
   return
           