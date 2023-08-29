# completa el código de la función
def suma_divisores(a):
  total = 0
  for i in range(1, a//2+1):
    total += i if not a%i else 0
    
  if total == 1:
    return total, True
  return total, False
