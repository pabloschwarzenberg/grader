def numero_perfecto(c):
  suma = 0
  for i in range(1,c):
    if (c % i == 0):
      suma += i
 
  if c == suma:
    return True
  else:
    return False
 