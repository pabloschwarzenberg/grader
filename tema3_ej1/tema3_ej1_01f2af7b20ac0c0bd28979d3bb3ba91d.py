# completa el código de la función
def suma_divisores(a):
  count = 0
  div = []
  for i in range(1 , a): 
    if a % i == 0: 
      div.append(i) 
      count += 1 
  if count == 1: 
    return sum(div), True
  else:
    return sum(div), False