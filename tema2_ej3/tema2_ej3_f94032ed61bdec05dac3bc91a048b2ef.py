def numero_perfecto(a):
  suma = 0
  for _ in range(1,a):
    if (a % _ == 0):
      suma += _
 
  if a == suma:
    return True
  else:
    return False
