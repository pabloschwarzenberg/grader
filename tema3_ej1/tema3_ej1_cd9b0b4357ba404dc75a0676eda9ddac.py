def suma_divisores(a):
  divi = []
  cont = 0
  for i in range(1 , a): 
    if a % i == 0: 
      divi.append(i) 
      cont += 1 
  if cont == 1: 
    return sum(divi), True
  else:
    return sum(divi), False