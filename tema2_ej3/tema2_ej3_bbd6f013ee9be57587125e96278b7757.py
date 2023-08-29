def numero_perfecto(a):
  s = 0
  for i in range(1,a-1):
    if a % i == 0:
      s += (i)
  if a == s:
    return True
  return False