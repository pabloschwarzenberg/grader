def suma_divisores(a):
  TotalDivisores=0
  for i in range (a+1):
    if a%(i+1)==0:
      TotalDivisores=TotalDivisores+1
  if TotalDivisores-1==1:
        return (a-(a-1), True)
  else:
        return (a-1, False)