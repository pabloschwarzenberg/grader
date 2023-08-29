def suma_divisores(j):
  div = []
  conta = 0
  for i in range(1 , j): 
    if j % i == 0: 
      div.append(i) 
      conta += 1 
  if conta == 1: 
    return sum(div), True
  else:
    return sum(div), False
