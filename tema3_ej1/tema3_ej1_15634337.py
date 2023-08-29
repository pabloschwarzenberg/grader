def suma_divisores(a):
  if a==1:
    return(0, False)
  c=0
  for i in range(1,a):
    if a%i==0:
      c=c+i
  if c==1:
    return (c,True)
  else:
    return (c,False)