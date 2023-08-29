def amigos(a,b):
  x = []
  y = []
  for i in range(1,a):
    if a%i == 0:
      x.append(i) 
  for j in range(1,b):
    if b%j == 0:
      y.append(j)
  if sum(x) == b and sum(y) == a:
    return True
  else:
    return False
