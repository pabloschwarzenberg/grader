def es_primo(x):
  if x<2:
    return False
  for l in range (2,x):
    if x % l == 0:
      print(x,l)
      return False
  return True