def suma_divisores(a):
  x = 0
  z = []
  for i in range(1,a+1):
    if a % i == 0:
      x += i
      z.append(str(i))
    else:
      continue
  x = x-a
  if len(z) == 2 and str(z[1]) == str(a):
    return x,True
  else:
    return x,False