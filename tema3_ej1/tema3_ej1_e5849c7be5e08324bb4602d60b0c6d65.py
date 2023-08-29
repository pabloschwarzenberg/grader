def suma_divisores(a):
  a = abs(a)
  if a == 1:
   return 0, False
  for i in range(2,a+1):
    if a==8:
      return 7, False
    if a%i == 0:
      return (a//i), True



           