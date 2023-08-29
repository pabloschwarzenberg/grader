def numero_perfecto(n):
  s = 0
  for i in range(1,n):
    if (n % (i) == 0):
      s += (i)
  if n == s:
    return True
  else:
    return False
    