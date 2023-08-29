      # completa el código de la función
def suma_divisores(a):
  numero = a
  i = 1
  cantidadDivisores = 0
  sumaDivisores = 0
  while i < numero:
    if(numero % i == 0):
      sumaDivisores += i
      cantidadDivisores += 1
    i += 1
  if(cantidadDivisores == 1):
    return (sumaDivisores,True)
  return (sumaDivisores,False)
