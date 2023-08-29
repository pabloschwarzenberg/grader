def suma_divisores(a):
  divisores = []
  contador = 0
  for i in range(1 , a): 
    if a % i == 0: 
      divisores.append(i) 
      contador += 1 
  if contador == 1: 
    return sum(divisores), True
  else:
    return sum(divisores), False