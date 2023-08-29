def suma_divisores(a):
  y = []
  for x in range(1, a):
    if a % x == 0:
      if a == x:
        y.append(0)
      else:
        y.append(x)
  z = False
  print(sum(y)%a)
  if sum(y) >= 1:
    if sum(y) == 1:
      z = True
    elif sum(y) == 0:
      z = True
  return(sum(y), z)