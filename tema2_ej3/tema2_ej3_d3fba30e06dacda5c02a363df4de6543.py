def numero_perfecto(n):
  s = 0
  for _ in range(1,n):
    if (n % _ == 0):
      s += _
 
  if n == s:
    return True
  else:
    return False