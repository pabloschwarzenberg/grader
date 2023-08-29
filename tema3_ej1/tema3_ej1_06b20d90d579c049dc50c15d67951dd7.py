def suma_divisores(el_numero):
  divisores = [1]
  for i in range(2, el_numero +1):
    if el_numero % i ==0:
      divisores.append(i)
  divisores.remove(el_numero)
  if sum(divisores) == 1:
    return sum(divisores),True
  else:
    return sum(divisores),False