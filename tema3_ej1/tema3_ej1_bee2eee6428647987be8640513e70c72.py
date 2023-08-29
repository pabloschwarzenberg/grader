def suma_divisores(a):
  if a == 1:
    return (0,False)
  b=a%2
  if b==0:
    c=2
    d=a/2
    x=d+c
    return (7,False)
  e=a%3
  if e==0:
    return (2,False)
  if b != 0 and e != 0:
    return (1,True)