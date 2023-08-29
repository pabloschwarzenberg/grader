# completa el código de la función
def suma_divisores(a):
  result = 0
  for i in range(1, a):
    if a % i == 0:
      result += i    
  if result ==1:
    return result,True
  else:
    return result,False

print(suma_divisores(1))