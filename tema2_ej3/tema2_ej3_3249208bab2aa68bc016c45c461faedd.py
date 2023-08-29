def suma_divisores(a):
    suma = 0
    for i in range(1,a):
      if a % i == 0:
        suma+=i
      elif suma == 1:
        return suma
    return suma 
def numero_perfecto(a):
  if suma_divisores(a) == a:
    return True
  else:
    return False
    
           