def numero_perfecto(A):
  suma = 0
  for i in range(1, A):
    if (A % (i) == 0):
      suma += (i)
  if A == suma:
    return True
  else:
    return False