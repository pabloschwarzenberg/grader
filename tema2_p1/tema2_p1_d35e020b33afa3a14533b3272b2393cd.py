def es_primo(numero):
  divisor=2
  if numero==1 or numero==0:
    return False
  if numero==divisor:
    return True
  while divisor<numero:
    if numero%divisor==0:
      return False
    else:
      return True
    divisor +=1
  return True
