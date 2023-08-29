def numero_perfecto(a):

  suma = 0

  for i in range(1, a):
    if numero % i == 0:
      suma += i
      
  if (suma == a):
    
    return True
  
  else:
    
    return False
