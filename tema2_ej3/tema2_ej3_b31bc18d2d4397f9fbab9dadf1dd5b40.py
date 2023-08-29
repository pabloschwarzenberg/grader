def suma_divisiones(n):
  s = 0
  for k in range(1, n+1):
    if n % k == 0:
      s += k
  return s 

def numero_perfecto(n):
  if (2 * n == suma_divisiones(n)):
    return True
  else:
    return False