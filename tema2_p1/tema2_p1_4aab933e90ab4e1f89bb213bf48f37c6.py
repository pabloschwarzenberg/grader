
def es_primo(x):
  if x<2:
    return (False)
  for n in range(2,x):
    if x%n == 0:
      return (False)
  return (True)
