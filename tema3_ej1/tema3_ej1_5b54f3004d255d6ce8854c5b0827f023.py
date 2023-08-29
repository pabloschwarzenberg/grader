def suma_divisores(a):
  sum = 0
  for i in range(1,a):
    if a % i ==0:
      sum = sum + i
  b = True
  if a <= 1:
    b = False
  elif a == 2:
    b = True
  else:
    for i in range(2,a):
      if a % i == 0:
        b = False
  return sum, b
  return sum, b           