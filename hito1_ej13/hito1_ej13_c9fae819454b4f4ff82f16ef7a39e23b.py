def factores_p(a):
  p=[]
  for i in range(2,a+1):
    while a % i == 0:
      p.append(i)
      a=a/i
  return(p)