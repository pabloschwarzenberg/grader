# completa el código de la función
def suma_divisores(a):
  suma = 0
  for i in range(1, int(a / 2) + 1):
    if a % i == 0:
      suma += i
  if suma == 1:
    return suma, True
  return suma, False
           