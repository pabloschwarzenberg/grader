def suma_divisores(a):
  dividir = []
  contar = 0
  for i in range(1 , a): 
    if a % i == 0: 
      dividir.append(i) 
      contar += 1 
  if contar == 1: 
    return sum(dividir), True
  else:
    return sum(dividir), False