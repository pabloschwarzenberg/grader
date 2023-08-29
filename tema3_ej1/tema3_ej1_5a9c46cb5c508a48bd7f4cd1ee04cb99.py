# completa el código de la función
def suma_divisores(a):
  sumaDivisores = 0
  for i in range(1,a):
    if a % i == 0 and a != i:
      sumaDivisores = sumaDivisores + i
  if sumaDivisores == 1:
    primo = True
  else:
    primo = False
  return sumaDivisores,primo        