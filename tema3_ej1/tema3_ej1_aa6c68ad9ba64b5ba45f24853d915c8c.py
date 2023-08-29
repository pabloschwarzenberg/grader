def suma_divisores(a):
  suma = 0
  for i in range(1,a):
    if a % i == 0:
       suma = suma + i

  x = True
  if a <=1:
     x = False
  elif a == 2 :
     x = True
  else:
    for i in range(2, a):
       if a % i == 0:
          x = False

  return (suma,x)