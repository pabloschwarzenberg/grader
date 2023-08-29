# completa el código de la función
def suma_divisores(a):
  return
def suma_divisores(a):
  valor = 0
  for i in range(1, a):
    if a % i == 0:
      valor += i    
  if valor ==1:
    return valor,True
  else:
    return valor,False

print(suma_divisores(1))      