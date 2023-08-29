def numero_perfecto(a):
  sda = 0
  for n in range(1,a):
    if (a % n == 0):
      sda += n
  if sda == a:  
    return True
  else:
    return False