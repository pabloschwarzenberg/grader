def numero_perfecto(a):
  sum = 0 
  for i in range(2, a + 1 ):
      aux = a / i
      aux_entero = a // i 
      if aux == aux_entero:
        sum = sum + aux_entero 
  if sum == a: 
    return True
  else:
    return False      