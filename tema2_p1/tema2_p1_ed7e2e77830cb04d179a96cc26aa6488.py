def es_primo(a):
  for i in range(2,a):
    if a%i == 0:
      return False
  if  a == 1:
    return False
  return True