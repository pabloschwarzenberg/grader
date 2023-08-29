def numero_perfecto(num):
  suma = 0
  for j in range(1,num):
    if (num % (j) == 0):
      suma += (j)
  if num ==suma:
    return True
  else:
    return False